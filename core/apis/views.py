
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import HttpResponse

### rest framework imports 

from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status

### other imports 

import json

### local import 

from ..models import Blog, Author
from .utils.serializer import Blog_serializer
### get token class 

class customeAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        response = super(customeAuthToken,self).post(request,*args,**kwargs)
        token = Token.objects.get(key=response.data['token'])

        user = token.user

        return Response({
            'token':token.key,
            'usernmae':user.username
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hello(request):
    return HttpResponse(f'Hello {request.user}')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_blog_by_id(request,id):
    try:
        blog = Blog.objects.get(id=id)

        try:
            author = Author.objects.get(username=blog.author)

        except:

            return Response({'error':f'No author is found for blog with id: {id}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except:
        return Response({'error':f'No blog is found with id : {id}'},status=status.HTTP_404_NOT_FOUND)
    
    response = {
        'title':blog.title,
        'data_of_publish':blog.date_of_publish,
        'author_username':author.username,
        'author_name':author.full_name,
        'author_email':author.email,
        'blog_content':blog.blog_content,
    }

    return Response(response)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def blogs(request):

    if request.method == 'POST':
        try:
            data = request.data
            title = data['title']
            content = data['content']
            if not isinstance(title,str) or not isinstance(content,str):
                raise ValueError('Title ad content should be a str')
            try:
                blog = Blog.objects.create(title=title,blog_content=content,author=request.user)
                return Response({'blog_id':blog.id},status=status.HTTP_201_CREATED)
            except:
                return Response({'error':'bad request'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error':'bad request'},status=status.HTTP_400_BAD_REQUEST)
        
    else:

        blogs = Blog.objects.all()
        serialized = Blog_serializer(blogs,many=True)
        return Response(serialized.data)

