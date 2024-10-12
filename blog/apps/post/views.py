from django.shortcuts import render
from .models import Post

# Create your views here.

def posts(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})