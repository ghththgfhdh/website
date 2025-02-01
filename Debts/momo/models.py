from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from taggit.managers import TaggableManager #help



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

#class Tags(models.Model):
    #tags = TaggableManager()

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def display_tags(self):
        return ', '.join(tags.name for tags in self.tags.all()[:3])
    
    display_tags.short_description = 'Tags'

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
