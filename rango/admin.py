from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PagesAdmin)
admin.site.register(UserProfile)
