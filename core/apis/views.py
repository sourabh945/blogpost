
from django.views.decorators.csrf import csrf_exempt

### rest framework imports 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

### other imports 

import json

### local import 

from ..models import Blog, Author

from .utils import serializer


@api_view(['GET'])
def get_blog_by_id(request,id):
    try:
        blog = Blog.objects.get(id=id)

    except:
        return Response({'error':f'No blog is found with id : {id}'},status=status.HTTP_404_NOT_FOUND)
    
    response = serializer.Blog_serializer(blog)

    return Response(response.data)

