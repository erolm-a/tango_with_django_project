from django.contrib import admin
from rango.models import Category, Page

class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PagesAdmin)
