from django.contrib import admin
from django.utils.html import format_html

from .notifications import notify_about_posts
from . import models

logo_url = 'https://channel.unichallenge.gr/assets/img/UniChallenge_logo.png'
admin.site.site_header = format_html("`<img src={url} height=50 width=50`>", url=logo_url)

class PostAdmin(admin.ModelAdmin):

    def publish_posts(modeladmin, request, queryset):
        for post in queryset:
            post.published = True
            post.save()

    def unpublish_posts(modeladmin, request, queryset):
        for post in queryset:
            post.published = False
            post.save()

    actions = [publish_posts, unpublish_posts, notify_about_posts]
    list_display = ['title', 'date', 'published', 'external']
    exclude = ['external_id']
    readonly_fields = ['external_source']

class PostSource(admin.ModelAdmin):
    list_display = ['name', 'feed_url']

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id']
    exclude = ['notification_token']

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
admin.site.register(models.PostSource, PostSource)
admin.site.register(models.Subscription, SubscriptionAdmin)
