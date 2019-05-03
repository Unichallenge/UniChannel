from rest_framework import serializers
from .models import Post, Tags, PostTags

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'link', 'date')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('id', 'tags')
