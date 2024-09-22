from django.shortcuts import render
from django.http import HttpResponse
from random import choice, shuffle
from .models import Post

# Create your views here.



def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {'posts': Post.objects.all()} # passing the context for the template so that the data can be used
    return render(request, 'blog/home.html', context=context) # specifying the app directory under which blog specific templates are stored

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    posts = Post.objects.all()
    shuffle(posts)
    return render(request, 'blog/about.html', context={'title': choice(posts[:3] + [{}]).get('title')})