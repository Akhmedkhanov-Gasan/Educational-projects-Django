from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post


def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(
        request,
        'blog/index.html',
        {'posts': latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {'all_posts': all_posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post-detail.html', {
        'post': post,
    })
