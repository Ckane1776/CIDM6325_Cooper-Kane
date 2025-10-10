from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    BlogPostListView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
    CategoryListView, 
    CategoryCreateView,
    CategoryUpdateView, 
    CategoryDeleteView,
    TagCreateView,
)

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Blog URLs
    path('blog/', BlogPostListView.as_view(), name='blog_list'), 
    path('blog/new/', BlogPostCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/new/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    # Tag URLs
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
]