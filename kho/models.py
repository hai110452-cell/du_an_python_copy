# usermusic/models.py
from django.db import models
from django.contrib.auth.models import User

class UserMusic(models.Model):
    TYPE_CHOICES = [
        ('download', 'Downloaded'),
        ('favorite', 'Favorite'),
        ('purchase', 'Purchased'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    audio = models.FileField(upload_to='kho/', null=True, blank=True)  # 👈 thêm null=True, blank=True
    
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    source_id = models.IntegerField(null=True, blank=True)
    source_type = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.type}"