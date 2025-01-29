from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'display_tag')
    list_filter = ("status", 'tag')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug')
        }),
        ('The Fun Part', {
            'fields': ('content', 'tag', 'status')
        }),
    )

admin.site.register(Tag)