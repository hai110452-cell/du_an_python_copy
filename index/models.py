from django.db import models

class Music(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='music/images/')
    audio = models.FileField(upload_to='music/audio/')
    def __str__(self):
        return self.title

class MusicHot(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='hot/images/')
    audio = models.FileField(upload_to='hot/audio/')
    def __str__(self):
        return self.title