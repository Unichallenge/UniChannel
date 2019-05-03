from django.db import models
from PIL import Image

class Post(models.Model):
        title = models.CharField(max_length=200)
        description = models.CharField(max_length=2000)
        image = models.ImageField(upload_to = 'img/', blank=True, null = True)
        link = models.CharField(max_length=1000)
        date = models.DateField(auto_now=True, null = True)

class Tags(models.Model):
        tags = models.CharField(max_length=100)

class PostTags(models.Model):
        post = models.ForeignKey(Post,on_delete=models.CASCADE)
        tags = models.ForeignKey(Tags,on_delete=models.CASCADE)
