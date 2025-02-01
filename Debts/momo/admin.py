from django.contrib import admin
from .models import Post #Tags

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'display_tags') #display_tags
    list_filter = ("status", 'tags')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug')
        }),
        ('The Fun Part', {
            'fields': ('content', 'tags', 'status') #tags
        }),
    )

#admin.site.register(Tags)