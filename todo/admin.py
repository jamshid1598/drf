from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import (
    Category,
    ToDo,
    Image,
)
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # ('name', 'slug', 'image', 'caption', )
    list_display =('name', 'slug',)
    list_display_links = ('name',)
    ordering = ('name', 'slug',)
    search_fields = ('name', 'slug')

    prepopulated_fields = {'slug': ['name',]}

    fieldsets = (
        ('Category', {
            "fields": (
                'name', 'slug', 'image', 'caption',
            ),
        }),
    )
    
admin.site.register(Category, CategoryAdmin)


class ImageTabularInline(admin.TabularInline):
    model = Image
    min_num = 1
class ToDoAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline]
    # ('category', 'task', 'slug', 'started', 'ended', 'completed', )
    list_display = ('category', 'task', 'slug', 'started', 'ended', 'completed',)
    list_display_links = ('task',)
    list_editable = ('category', 'slug', 'started', 'ended', 'completed',)
    ordering = ('category', 'task', 'slug', 'started', 'ended', 'completed',)
    search_fields = ('category', 'task', 'slug', 'started', 'ended', 'completed',)

    prepopulated_fields = {'slug': ['task',]}

    fieldsets = (
        ('ToDo Detail', {
            'fields': (
                'category', 'task', 'slug', 'started', 'ended', 'completed'
            ),
        }),
    )

admin.site.register(ToDo, ToDoAdmin)