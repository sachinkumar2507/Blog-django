from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
