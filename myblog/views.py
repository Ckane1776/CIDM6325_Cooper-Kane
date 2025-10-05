from django.shortcuts import render
from .models import BlogPost  # Adjust model name if needed

def blog_view(request):
    posts = BlogPost.objects.all()
    return render(request, 'myblog/blog_view.html', {'posts': posts})
