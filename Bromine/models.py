from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class MyBlogInfo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    date_made = models.DateTimeField(default=timezone.now, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True, blank=True, default='coding')               # Category field
    #content = models.TextField(null=True, blank=True)
    content= RichTextField(blank = True, null = True)
    Likes = models.ManyToManyField(User, related_name='blog_posts')

    
    def total_likes(self):
            return self.Likes.count()
         
         
    def __str__(self): 
        return self.title
        
    def get_absolute_url(self):
        return reverse('home')
    

class Category(models.Model):                               # Category class
        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name
        
        def get_absolute_url(self):
            return reverse('home')
        

class Comment(models.Model):
    post = models.ForeignKey(MyBlogInfo, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)  # '%s - %s' % is very important
    


class Profile(models.Model):
     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
     bio = models.TextField()
     profile_photo = models.ImageField(null=True, blank=True, upload_to='images/')
     title = models.CharField(max_length=255, null=True, blank=True)
     twitter_url = models.CharField(max_length=255, null=True, blank=True)
     facebook_url = models.CharField(max_length=255, null=True, blank=True)


     def __str__(self): 
        return str(self.user)
     
     def get_absolute_url(self):
        return reverse('home')