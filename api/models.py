from django.db import models

# Create your models here.
from django.db.models.signals import pre_save

from Article_Publication.utils import unique_slug_generator


class Post(models.Model):
    title = models.CharField(max_length=128)
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique = True, max_length=250, null=True, blank=True, editable = False)
    text = models.TextField()

    def __str__(self):
        return self.title



"""
method: Generates Unique Slugs based on title and stores in Database
"""
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender = Post)


class Comment(models.Model):
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    post = models.ForeignKey(Post,related_name= "Post_Comment", on_delete=models.CASCADE)
    def __str__(self):
        return self.text