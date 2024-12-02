from django.urls import path 
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('newBlog/',createNewBlog,name='create_blog'),
    path('logout/for/you',logout_page,name='logout')
]   