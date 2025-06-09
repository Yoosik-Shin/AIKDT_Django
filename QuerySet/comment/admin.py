from django.contrib import admin

# Register your models here.
# admin.py
from .models import Comment
admin.site.register(Comment)