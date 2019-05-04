from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('tags/', views.TagsList.as_view(), name='taglist')
    re_path(r'^tags/?$', views.TagsList.as_view()),
    # re_path(r'^posts/?$', views.PostList.as_view()),
    re_path ( r'^posts/(?P<post>[\w,\s_]+)/?$', views.PostTitleList.as_view () ),
    re_path ( r'^posts/tags/(?P<tag>[\w,_]+)/?$', views.PostTagsList.as_view () ),
    re_path ( r'^posts/?$', views.PostList.as_view () ),
]+ static("/media/", document_root=settings.MEDIA_ROOT)

# Adding this lets you use filename extensions on URLs to provide an endpoint for a given media type.
# For example you can get endpoint data in json representation or html static file
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
