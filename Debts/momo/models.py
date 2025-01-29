from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        help_text="Helps sort blog posts. How would you describe the basic idea of the post in one word?"
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("genre_detail", args=[str(self.id)])
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "genre already exists (case insensitive match)"
            )
        ]

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(
        Tag, help_text="Add tags to post")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def display_tag(self):
        return ', '.join(tag.name for tag in self.tag.all()[:3])
    
    display_tag.short_description = 'Tag'

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
