from django.urls import path

from .views import *

urlpatterns = [
    path('hello/',helloworld,name='hello'),
    path('login/',login_page,name='login'),
    path('signup/',signup_page,name='signup')
]