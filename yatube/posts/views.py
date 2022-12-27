from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse
from django.conf import settings

from .models import Post, Group
from .forms import PostForm
from django.contrib.auth.models import User


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.POSTS_ON_MAIN)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'posts': post_list,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group_with_slug = Group.objects.get(slug=slug)
    post_list = Group.objects.filter(slug=group_with_slug)

    paginator = Paginator(post_list, settings.POSTS_ON_MAIN)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'posts': post_list,
        'group': group_with_slug,

    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    post_list = Post.objects.filter(author=user)

    paginator = Paginator(post_list, settings.POSTS_ON_MAIN)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'posts': post_list,
        'usermodel': user,

    }

    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    onepost = Post.objects.get(id=post_id)
    context = {
        'onepost': onepost,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            user = request.user

            return redirect(f'/profile/{user.username}/')

        return render(request, 'posts/profile.html', {'form': form})

    form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post_edited = PostForm(instance=post, data=request.POST)
        post_edited.save(commit=False)
        post_edited.author = request.user
        post_edited.save()
        return redirect(f'/posts/{post_id}/')

    form = PostForm(instance=post)
    is_edit = 'is_edit'
    contex = {
        'post': post,
        'form': form,
        'is_edit': is_edit
    }
    return render(request, 'posts/update_post.html', contex)
