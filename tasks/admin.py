from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Task, Users

@admin.register(Task)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

@admin.register(Users)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "email")