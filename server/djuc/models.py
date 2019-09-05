from django.db import models
from django.core.validators import RegexValidator
from django.db.models.signals import post_init
from django.dispatch import receiver
from datetime import date
import uuid
import feedparser

https = RegexValidator(r'^https://.*$', "The link should begin with https://")

class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

class PostSource(models.Model):
    name = models.CharField(max_length=100)
    feed_url = models.CharField(max_length=2000)

    auto_publish = models.BooleanField(
        default=False,
        help_text='Posts retrieved from this source get published automatically.'
    )
    auto_unpublish = models.BooleanField(
        default=True,
        help_text='Posts retrieved from this source get unpublished if removed from the source.'
    )
    auto_tags = models.ManyToManyField(Tag, 
        blank=True,
        help_text='Tags to get applied automatically when retrieved.'
    )

    def __str__(self):
        return self.name

@receiver(post_init, sender=PostSource)
def post_source_init(sender, instance, **kwargs):
    pass

class Post(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.CharField(max_length=2000, validators=[https])
    date = models.DateField(default=date.today, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    published = models.BooleanField(default=True)

    external = models.BooleanField(
        default=False,
        help_text='Posts that are marked as external get updated if changes to \
            the source are made.'
    )
    external_id = models.CharField(max_length=255, unique=True, null=True)
    external_source = models.ForeignKey(PostSource, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date']
        permissions = [
            ('can_publish', 'Publish/unpublish posts'),
        ]

    def __str__(self):
        return self.title

class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    notification_token = models.TextField()