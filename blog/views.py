from django.shortcuts import render
from django.http import HttpResponse
from random import choice, shuffle
from .models import Post, User

# Create your views here.

def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    posts = list(Post.objects.all())

    context = {'posts': posts} # passing the context for the template so that the data can be used
    users = list(User.objects.all())
    # for post in posts_:
    #     post.pop('author')
    #     post.pop('date_posted')
    #     new_post = Post(**post)
    #     new_post.author = choice(users)
    #     new_post.save()
    # for post in posts:
    #     post.author = choice(users)
    #     post.save()
    return render(request, 'blog/home.html', context=context) # specifying the app directory under which blog specific templates are stored

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    posts = list(Post.objects.all())
    shuffle(posts)
    return render(request, 'blog/about.html', context={'title': choice(posts[:3]).title})