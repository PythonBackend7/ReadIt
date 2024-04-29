from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Tag, Contact, Category, HappyClients, Post
from .forms import ContactForm


# Create your views here.


def home_view(request):
    posts = Post.objects.all().order_by('-created_at')[:6]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def about_view(request):
    about = Team.objects.all()
    happy_clients = HappyClients.objects.all().order_by('-created_at')
    context = {'about': about, 'happy_clients': happy_clients}
    return render(request, 'about.html', context)


def articles_view(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
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
    post = get_object_or_404(Post, id=pk)
    tags = Tag.objects.all()
    cats = Category.objects.all()
    recent_posts = Post.objects.all().order_by('-created_at')[:3]
    tag = request.GET.get('tag')
    if tag:
        post = Post.objects.filter(tags__name__contains=tag)
    q = request.GET.get('q')
    if q:
        post = Post.objects.filter(title__icontains=q)
    context = {'post': post, 'tags': tags, 'cats': cats, 'recent_posts': recent_posts}
    return render(request, 'blog-single.html', context)
