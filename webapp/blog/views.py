from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import InstaPost, GithubPost

def get_instagram_posts():
    return InstaPost.objects.all()

def get_github_projects():
    return GithubPost.objects.all()

def home(request):
    template = loader.get_template('blog/index.html')
    context = {
        'posts': get_instagram_posts(),
        'github': get_github_projects(),
    }
    return HttpResponse(template.render(context, request))
    