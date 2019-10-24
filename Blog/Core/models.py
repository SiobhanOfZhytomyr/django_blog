from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()



class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(to=User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=70,unique=True)
    keywords = models.ManyToManyField(to=Keyword, related_name="posts", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Core:post-detail', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ('-created', 'title')


