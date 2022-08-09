from pydoc_data.topics import topics
from django.shortcuts import render, redirect
from django.contrib import messages
from base.models import Blog, Category, Comment, Event

# Create your views here.
def home(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def community(request):
    context = {}
    return render(request, 'base/community.html', context)

def forum(request):
    context = {}
    return render(request, 'base/forum.html', context)

def event(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'base/event.html', context)

def eventSingle(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'base/eventSingle.html', context)

def blog(request):
    blogs = Blog.objects.all()
    comments = Comment.objects.all()
    topics = Category.objects.all()
    context = {'blogs': blogs, 'topics': topics, 'comments': comments}
    return render(request, 'base/blog.html', context)

def blogSingle(request, pk):
    blog = Blog.objects.get(id=pk)
    topics = Category.objects.all()
    context = {'blog': blog, 'topics': topics}
    return render(request, 'base/blogSingle.html', context)

def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)