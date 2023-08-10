from django.contrib import admin
from .models import MyBlogInfo, Category, Comment, Profile

# Register your models here.


admin.site.register(MyBlogInfo)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)
