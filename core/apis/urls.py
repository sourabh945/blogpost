from django.urls import path

## local imports 

from . import views 

urlpatterns = [
    path('api/posts',views.blogs,name='blogs'),
    path('api/posts/<str:id>',views.get_blog_by_id,name='blogByID'),
    path('api/get-token',views.customeAuthToken.as_view(),name='get_api_token'),
    path('api/hello',views.hello,name='api_hello')
]