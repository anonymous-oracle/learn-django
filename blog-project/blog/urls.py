from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='blog-user-posts'),
    # pk - primary key of the post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete/', views.PostDeletelView.as_view(), name='blog-post-delete'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-post-create'),
    path('about/', views.about, name='blog-about'),
]