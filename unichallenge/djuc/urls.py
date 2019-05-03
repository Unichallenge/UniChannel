from django.urls import path

from . import views

urlpatterns = [
    path('tags/', views.TagsList.as_view(), name='taglist')
]
