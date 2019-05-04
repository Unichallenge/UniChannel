from rest_framework import serializers
from .models import Post, Tags, PostTags

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image', 'link', 'date', 'tags')
        depth = 1

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ('id', 'tags')
