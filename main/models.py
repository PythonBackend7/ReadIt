from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.title


class HappyClients(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author/')
    description = models.TextField()
    def __str__(self):
        return self.name


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='comments/', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name
