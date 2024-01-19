from django.contrib import admin

# Register your models here.
from .models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','address','phone_number']
admin.site.register(Student,StudentAdmin)



class BooksSerializer(admin.ModelAdmin):
    list_display=['title','genre','price']
admin.site.register(Books,BooksSerializer)    
    
    
    
    
