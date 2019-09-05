from django.db.models import Q

from rest_framework import generics
from rest_framework import permissions

from .models import Tag, Post
from .serializers import TagSerializer, PostSerializer


class TagsList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Tag.objects.all()
        term = self.kwargs['term']
        if term is not None:
            queryset = queryset.filter(tag_name__icontains=term)[:10]
        return queryset


class PostsByAll(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        term = self.kwargs['term']
        tag_ids = Tag.objects.filter(tag_name__iexact=term).values('id')
        return Post.objects.filter(published=True).filter(
            Q(title__icontains=term) | Q(tags__in=tag_ids)
        )

class PostsByTag(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        term = self.kwargs['term']
        tag_ids = Tag.objects.filter(tag_name__iexact=term).values('id')
        return Post.objects.filter(published=True).filter(tags__in=tag_ids)

class PostTitleList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        posts = self.kwargs['post'].split(',')
        post_ids = Post.objects.filter(title__in=posts).values('id')
        return Post.objects.filter(published=True).filter(id__in=post_ids)


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return Post.objects.filter(published=True)
