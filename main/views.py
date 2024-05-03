from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Tag, Contact, Category, HappyClients, Post, Comment
from .forms import ContactForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home_view(request):
    posts = Post.objects.all().order_by('-created_at')[:6]
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'index.html', context)


def about_view(request):
    about = Team.objects.all()
    happy_clients = HappyClients.objects.all().order_by('-created_at')
    context = {'about': about, 'happy_clients': happy_clients}
    return render(request, 'about.html', context)


def articles_view(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(title__icontains=search)
    context = {'posts': posts,
               'q': search}
    return render(request, 'blog.html', context)


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def article_detail_view(request, pk):
    form = CommentForm()
    post = get_object_or_404(Post, id=pk)
    tags = Tag.objects.all()
    cats = Category.objects.all()
    recent_posts = Post.objects.all().order_by('-created_at')[:3]
    comments = Comment.objects.filter(post__id=pk).order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # comment = form.save(commit=False)
            # comment.post = post
            # comment.save()
            form.save()
            return redirect(f'/blog/{post.id}')
    tag = request.GET.get('tag')
    if tag:
        post = Post.objects.filter(tags__name=tag)
    context = {'post': post,
               'tags': tags,
               'cats': cats,
               'comments': comments,
               'recent_posts': recent_posts,
               'form': form,
               }
    return render(request, 'blog-single.html', context)
