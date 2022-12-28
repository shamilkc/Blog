from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150,unique=True)


    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(BlogPost,related_name='post',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    text = models.TextField()
    

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    approved_comment = models.BooleanField(default=True)

    