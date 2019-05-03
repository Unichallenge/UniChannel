from django.contrib import admin

from .models import Post, Tags, PostTags

admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(PostTags)
