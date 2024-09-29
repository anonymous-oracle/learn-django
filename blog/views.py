from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from random import choice, shuffle
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, User

# Create your views here.

# def home(request):
#     # return HttpResponse('<h1>Blog Home</h1>')
#     posts = list(Post.objects.all())

#     context = {'posts': posts} # passing the context for the template so that the data can be used
#     users = list(User.objects.all())
#     # for post in posts_:
#     #     post.pop('author')
#     #     post.pop('date_posted')
#     #     new_post = Post(**post)
#     #     new_post.author = choice(users)
#     #     new_post.save()
#     # for post in posts:
#     #     post.author = choice(users)
#     #     post.save()
#     return render(request, 'blog/home.html', context=context) # specifying the app directory under which blog specific templates are stored


class PostListView(ListView):
    model = Post # attaches the view class to the model we meant for it to use

    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html' # points to the template that the class view must use

    context_object_name = 'posts' # the 'posts' variable is the context passed to the template where the data will be rendered; the View can look for this variable to render the data
    
    # ordering = ['date_posted'] # oldest post first
    ordering = ['-date_posted'] # newest post first
    
    paginate_by = 5 # in the URL add ?page=2 to go to the next page

class UserPostListView(ListView):
    model = Post
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' 
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    # based on <app>/<model>_<viewtype>.html naming convention, this view class will look for blog/post_detail.html template

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] # this will need post_form.html as the template

    def form_valid(self, form):
        form.instance.author = self.request.user # the form being submitted belongs to the current logged in Author, for LoginRequiredMixin
        return super().form_valid(form) # sets the author

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # make sure only the author of the post can update the post
    model = Post
    fields = ['title', 'content'] # this will need post_form.html as the template

    def form_valid(self, form):
        form.instance.author = self.request.user # the form being submitted belongs to the current logged in Author
        return super().form_valid(form) # sets the author
    
    def test_func(self): # override function for UserPassesTestMixin
        post = self.get_object() # gets the object model variable is set to
        if self.request.user == post.author:
            return True
        return False

class PostDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # redirects on successful deletion to homepage

    def test_func(self): # override function for UserPassesTestMixin
        post = self.get_object() # gets the object model variable is set to
        if self.request.user == post.author:
            return True
        return False

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    posts = list(Post.objects.all())
    shuffle(posts)
    return render(request, 'blog/about.html', context={'title': choice(posts[:3]).title})