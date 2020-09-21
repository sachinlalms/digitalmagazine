from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.urls import reverse

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=100,unique='true')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=2000, default='https://cdn.flipsnack.com/blog/wp-content/uploads/2018/03/09163921/Cover.png')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post-details', kwargs={'pk': self.pk})

class Meta:
    odering =['-created_on']

    def __str__(self):
        return self.title



