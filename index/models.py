from django.db import models

class Music(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title

class MusicHot(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title