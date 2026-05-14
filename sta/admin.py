from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Note, Category, CustomUser, department
# Register your models here.

admin.site.register(Note)
admin.site.register(Category)
admin.site.register(CustomUser)
admin.site.register(department)



