from .models import Tags
from .serializers import TagSerializer
from django.contrib.staticfiles import views

from rest_framework import permissions
from rest_framework import generics

class TagsList(generics.ListCreateAPIView):
    serializer_class =  TagSerializer

    def get_queryset(self):
        queryset = Tags.objects.all()
        tag_name = self.request.query_params.get('tags', None)
        if tag_name is not None:
            queryset = queryset.filter(tags__contains=tag_name)
        return queryset
