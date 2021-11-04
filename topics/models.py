from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=256,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=200,blank = True)
    difficulty = models.IntegerField(default=0)
    category = models.ForeignKey(Category,related_name='topics',on_delete=models.CASCADE,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self) :
        return self.title


class Resource(models.Model):
    link = models.URLField(blank=True)
    topic = models.ForeignKey(Topic,related_name='resources',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.link

class Problem(models.Model):
    link = models.URLField(blank=True)
    topic = models.ForeignKey(Topic,related_name='problems',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.link

class Template(models.Model):
    link = models.URLField(blank=True)
    topic = models.ForeignKey(Topic,related_name='templates',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.link