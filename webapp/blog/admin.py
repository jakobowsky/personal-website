from django.contrib import admin
from .models import InstaPost, GithubPost
# Register your models here.
admin.site.register(InstaPost)
admin.site.register(GithubPost)