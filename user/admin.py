from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['created_at', 'updated_at', 'active']
    list_display = ['user']