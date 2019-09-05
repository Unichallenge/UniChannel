from rest_framework import serializers

from .models import Post, Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'description', 'image', 'link', 'date', 'tags', 
            'external', 'external_source'
        )
        depth = 1


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')
