from django.db import models

# Create your models here.
class Category(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='category/images/', null=True, blank=True)
    audio = models.FileField(upload_to='category/audio/', null=True, blank=True)
    def __str__(self):
        return self.title
    

class Rock(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='rock/images/', null=True, blank=True)
    audio = models.FileField(upload_to='rock/audio/', null=True, blank=True)
    def __str__(self):
        return self.title
    

class Edm(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='edm/images/', null=True, blank=True)
    audio = models.FileField(upload_to='edm/audio/', null=True, blank=True)
    def __str__(self):
        return self.title
    


    

class Ballad(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='ballad/images/', null=True, blank=True)
    audio = models.FileField(upload_to='ballad/audio/', null=True, blank=True)
    def __str__(self):
        return self.title
    


    

class Viet(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='viet/images/', null=True, blank=True)
    audio = models.FileField(upload_to='viet/audio/', null=True, blank=True)
    def __str__(self):
        return self.title
    

class Hiprap(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='hiprap/images/', null=True, blank=True)
    audio = models.FileField(upload_to='hiprap/audio/', null=True, blank=True)
    def __str__(self):
        return self.title
