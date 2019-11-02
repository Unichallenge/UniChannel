from firebase_admin import messaging
from background_task import background

from .models import Post, Subscription
from .views import CsrfExemptSessionAuthentication

from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

import sentry_sdk

def notify_about_posts(modeladmin, request, queryset):
    for id in queryset.values_list('id', flat=True):
        notify_about_post_async(id)

@background()
def notify_about_post_async(post_id):
    post = Post.objects.get(id=post_id)
    
    notification = messaging.Notification(
        title=post.title,
        body=post.description,
    )
    webpush = messaging.WebpushConfig(
        fcm_options=messaging.WebpushFCMOptions(
            link=post.link
        )
    )

    for sub in Subscription.objects.all():
        try:
            message = messaging.Message(
                notification=notification,
                token=sub.notification_token,
                webpush=webpush
            )
            messaging.send(message)

            print('Subscription %s notified about %s\
                   successfully!' % (sub.id, post.id))

        except Exception as e:
            sentry_sdk.capture_exception(e)
            raise e

class NotificationView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, format=None):
        token = request.data['token']
        subscription = Subscription(notification_token=token)
        subscription.save()

        content = { 'id': subscription.id }
        return Response(content)

class NotificationDeleteView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def delete(self, request, format=None):
        id = request.query_params['token']
        Subscription.objects.filter(id__exact=id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)