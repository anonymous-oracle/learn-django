from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # passing the function for execution when the object and the field is created
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | created on {self.date_posted.strftime("%d-%m-%Y %H:%M:%S")} by {self.author.username}"
    
    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk':self.pk}) # kwargs is the url parameter send to the post detail URL