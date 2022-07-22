from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.

def post_list (request):
    posts = Post.objects.all().order_by('published_date')
    context={
        'posts':posts
    }
    return render(request, 'blog/post_list.html', context)

def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    context={
        'post':post
    }
    return render(request, 'blog/post_details.html', context)

def post_new (request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form= PostForm()
    context={
        'form':form
    }
    return render(request, 'blog/post_edit.html', context)

def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == Post:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context={
        'form':form
    }

    return render(request, 'blog/post_edit.html', context)