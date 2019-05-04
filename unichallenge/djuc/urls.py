from django.urls import path, re_path

from . import views

urlpatterns = [
    # path('tags/', views.TagsList.as_view(), name='taglist')
    re_path(r'^tags/?$', views.TagsList.as_view()),
    # re_path(r'^posts/?$', views.PostList.as_view()),
    re_path ( r'^posts/(?P<post>[\w,\s_]+)/?$', views.PostList.as_view () ),
    re_path ( r'^posts/tags/(?P<tag>[\w,_]+)/?$', views.PostTagsList.as_view () )
]
