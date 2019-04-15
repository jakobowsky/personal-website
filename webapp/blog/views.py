from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import InstaPost

def get_instagram_posts():
    return InstaPost.objects.all()


def home(request):
    template = loader.get_template('blog/index.html')
    context = {
        'posts': get_instagram_posts()
    }
    return HttpResponse(template.render(context, request))
    