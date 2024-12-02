from django.urls import path

## local imports 

from . import views 

urlpatterns = [
    path('api/posts',views.blogs,name='blogs'),
    path('api/posts/<str:id>',views.get_blog_by_id,name='blogByID'),

]