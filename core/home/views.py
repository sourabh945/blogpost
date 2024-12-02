from django.shortcuts import render ,redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.middleware.csrf import get_token
from django.core.exceptions import ValidationError


### local imports 

from ..models import Blog


@login_required
def home(request):
    return render(request,'home_page/index.html')

@login_required
def createNewBlog(request):
    if request.method == 'POST':
        try:
            title = request.data['title']
            content = request.data['content']
            if not isinstance(title,str) or not isinstance(content,str):
                raise ValidationError()
            blog = Blog.objects.create(title=title,blog_content=content)
            return redirect('home')
        except:
            return ValidationError()
    token = get_token(request)
    return render(request,'create_blog/index.html',content_type={'csrf_token':token})

@login_required
def logout_page(request):
    logout(request)
    return redirect('login')