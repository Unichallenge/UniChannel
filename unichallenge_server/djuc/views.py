from rest_framework import generics
from rest_framework import permissions

from .models import Tags, Post, PostTags
from .serializers import TagSerializer, PostSerializer


class TagsList(generics.ListCreateAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tags.objects.all()
        tag_name = self.request.query_params.get('tag', None)
        if tag_name is not None:
            queryset = queryset.filter(tags__icontains=tag_name)[:10]
        return queryset


class PostTagsList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        tags = self.kwargs['tag'].split(',')
        tag_ids = Tags.objects.filter(tags__in=tags).values('id')
        post_ids = PostTags.objects.filter(tags_id__in=tag_ids).values('post_id')
        return Post.objects.filter(id__in=post_ids)


class PostTitleList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        posts = self.kwargs['post'].split(',')
        post_ids = Post.objects.filter(title__in=posts).values('id')
        return Post.objects.filter(id__in=post_ids)


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Post.objects.order_by('-date')
