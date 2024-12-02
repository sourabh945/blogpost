from django.shortcuts import render , redirect , HttpResponse , HttpResponsePermanentRedirect
from django.contrib.auth import authenticate , login 
from django.contrib.auth.decorators import login_required
from django.db.models import Q as q_
from django.middleware.csrf import get_token
from django.contrib import messages

### local imports

from .forms import login_form , signup_form
from ..models import Author as User


@login_required
def helloworld(request):
    return HttpResponse(f'Hello {request.user.username}, I hope you are doing well and i thank you for using this serivce \n -owner: sheokand.sourabh.anil@gmail.com')


def signup_page(request):
    """Page for signup the user"""
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                email=email,
                username=username,
                name=name,
                password=password
            )
            if user:
                return redirect('login')
            else:
                messages.error(request=request,message='Username or email is already exists',extra_tags='login')
                return redirect('login')
        else:
            messages.error(request=request,message='Username or email is already exists',extra_tags='login')
            return redirect('login')
    else:
        login_ = login_form()
        signup_ = signup_form()
        context = {'csrf_token':get_token(request),'login_form':login_,'signup_form':signup_}
        return render(request,'login/index2.html',context)

def login_page(request):
    """Page for login the user"""
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = User.objects.get( q_(username=username_or_email) | q_(email=username_or_email) )
            user = authenticate(request,username=user.username,password=password)
            if user:
                login(request,user)

                """
                redirect to the user panel
                """
                return redirect('hello')
            
            else:
                messages.error(request=request,message='Invalid credentials',extra_tags='login')
                return redirect('login')
        else:
            messages.error(request=request,message='User is not registered',extra_tags='signup')
            return redirect('signup')
        
    else:
        login_ = login_form()
        signup_ = signup_form()
        context = {'csrf_token':get_token(request),'login_form':login_,'signup_form':signup_}
        return render(request,'login/index2.html',context)