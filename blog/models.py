from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helper import *

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    content = FroalaField()
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='blog')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self.title)
        super(Post, self).save(*args, **kwargs)
