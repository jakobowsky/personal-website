from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def get_instagram_posts():
    pass


def home(request):
    template = loader.get_template('blog/index.html')
    context = {
        'test': '123'
    }
    return HttpResponse(template.render(context, request))
    