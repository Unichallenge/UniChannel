from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import notifications
from . import sources

urlpatterns = [
    re_path ( r'^posts/(?P<post>[\w,\s_]+)/?$', views.PostTitleList.as_view () ),
    re_path ( r'^posts/?$', views.PostList.as_view () ),
    re_path ( r'^tag/search/(?P<term>[\w,_]+)/?$', views.TagsList.as_view()),
    re_path ( r'^post/search/(?P<term>[\w,\s_]+)/?$', views.PostsByAll.as_view () ),
    re_path ( r'^post/search/#(?P<term>[\w,\s_]+)/?$', views.PostsByTag.as_view () ),
    re_path ( r'^notifications/subscribe$', notifications.NotificationView.as_view () ),
    re_path ( r'^notifications/unsubscribe$', notifications.NotificationDeleteView.as_view () )
]

urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT)

# Adding this lets you use filename extensions on URLs to provide an endpoint for a given media type.
# For example you can get endpoint data in json representation or html static file
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

# sources.read_sources(schedule=3, repeat=10)