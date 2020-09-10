from django.contrib.auth.models import User
from django.db import models

# Create your models here.
STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=100,unique='true')
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content =models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
