from django.db import models

# Create your models here.
class Category(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='category/images/')
    audio = models.FileField(upload_to='category/audio/')
    def __str__(self):
        return self.title
    

class Rock(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='rock/images/')
    audio = models.FileField(upload_to='rock/audio/')
    def __str__(self):
        return self.title
    

class Edm(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='edm/images/')
    audio = models.FileField(upload_to='edm/audio/')
    def __str__(self):
        return self.title
    


    

class Ballad(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='ballad/images/')
    audio = models.FileField(upload_to='ballad/audio/')
    def __str__(self):
        return self.title
    


    

class Viet(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='viet/images/')
    audio = models.FileField(upload_to='viet/audio/')
    def __str__(self):
        return self.title
    

class Hiprap(models.Model):
    date = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='hiprap/images/')
    audio = models.FileField(upload_to='hiprap/audio/')
    def __str__(self):
        return self.title