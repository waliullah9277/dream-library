from django.contrib import admin
from .import models
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ['category_name', 'slug',]

admin.site.register(models.CategoryModel,CategoryAdmin)