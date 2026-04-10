from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(null=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    

class Rock(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(null=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    

class Edm(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(null=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    


    

class Ballad(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(null=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    


    

class Viet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(null=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    

class Hiprap(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    image = models.ImageField(null=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    
    def __str__(self):
        return self.title