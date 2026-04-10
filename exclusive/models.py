from django.db import models

# Create your models here.
class ExclusiveItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='exclusive/', null=True, blank=True)
    audio = models.FileField(upload_to='exclusive/audio/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title