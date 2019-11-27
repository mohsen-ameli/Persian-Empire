from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

urlpatterns = [
    path('', PostListView.as_view (), name='home-blog'),
    path('user/<str:username>', UserPostListView.as_view (), name='user-post'),
    path('post/<int:pk>', PostDetailView.as_view (), name='post-detail'),
    path('post/new/', PostCreateView.as_view (), name='new-post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view (), name='update-post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view (), name='delete-post'),
    path ('about/', views.About, name='blog-about'),
    path('bootstrap.html/', views.bootstrap, name='bootstrap'),
    path('Nuno.html/', views.nuno, name='nuno'),
]
