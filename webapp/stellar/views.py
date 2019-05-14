from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('stellar/index2.html')
    context = {'':''}
    return HttpResponse(template.render(context, request))