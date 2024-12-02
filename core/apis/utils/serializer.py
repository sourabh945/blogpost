from rest_framework import serializers
from ...models import Blog

class Blog_serializer(serializers):
    class Meta:
        model = Blog
        fields = ['id','title','author','date_of_publish','blog_content']