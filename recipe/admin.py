from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Post

class CustomModelAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date')
    list_display = ['author', 'recipe']

admin.site.register(Post,CustomModelAdmin)