from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Community)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Dynamic)
admin.site.register(Chat)
admin.site.register(Product)

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'image', 'price']
#     list_editable = ['name', 'price']

# admin.site.register(Product, ProductAdmin)
