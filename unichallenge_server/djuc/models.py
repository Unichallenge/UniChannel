from django.db import models


class Tags(models.Model):
    tags = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True, null=True)
    tags = models.ManyToManyField(Tags, through='PostTags')


class PostTags(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
