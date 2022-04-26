from django.contrib import admin
from .models import Post, Category,Profile

admin.site.register(Post) # admin can access 'Post'
admin.site.register(Category)# admin can access 'Catagory'
admin.site.register(Profile)# admin can access 'Catagory'
# Register your models here.
