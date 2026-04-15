
from rest_framework import serializers
from .models import UserMusic

class UserMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMusic
        fields = '__all__'