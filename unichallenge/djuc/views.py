from .models import Tags
from .serializers import TagSerializer, PostSerializer
from django.contrib.staticfiles import views
from .retrieval import getPosts
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import permissions
from rest_framework import generics

class TagsList(generics.ListCreateAPIView):
    serializer_class =  TagSerializer

    def get_queryset(self):
        queryset = Tags.objects.all()
        tag_name = self.request.query_params.get('tag', None)
        if tag_name is not None:
            queryset = queryset.filter(tags__icontains=tag_name)
        return queryset

# class PostList(APIView):
#
#     def get(self, request, format=None):
#         d = {}
#         bookfields = ['title', 'description', 'image', 'link', 'date']
#         tag_name = self.request.query_params.get('tag', None)
#         if tag_name is None:
#             return Response()
#         fulllist = fb.findbooks(str(isbn), None, True)
#         firstbook = fulllist[0]
#         for i in range(len(firstbook)):
#             d[bookfields[i]] = firstbook[i]
#         return Response(d)

    # def get(self, request):
    #     tag_name = self.request.query_params.get('tag', None)
    #     post_list = getPosts(tag_name)
    #
    #     return JsonResponse(post_list, safe=False)