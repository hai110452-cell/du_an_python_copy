from django.db import models

# Create your models here.
class Category(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
    

class Rock(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
    

class Edm(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
    


    

class Ballad(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
    


    

class Viet(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
    

class Hiprap(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title