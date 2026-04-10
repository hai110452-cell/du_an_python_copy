from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)

class MusicHot(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(upload_to='rock/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    def __str__(self):
        return self.title