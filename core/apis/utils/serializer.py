from rest_framework import serializers
from ...models import Blog

class Blog_serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title','author','date_of_publish','blog_content']