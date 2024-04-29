from django.contrib import admin
from .models import Category, Tag, Contact, Post, HappyClients, Team


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'category',)
    list_display_links = ('id', 'title',)
    filter_horizontal = ('tags',)
    search_fields = ('title', 'category',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(Post, PostAdmin)
admin.site.register(HappyClients)
admin.site.register(Team)
