from django.contrib import admin
from .models import Student
# Register your models here.

"""by this we can see our table in admin side"""
@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']