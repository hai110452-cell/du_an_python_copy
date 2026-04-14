from rest_framework import serializers
from .models import Music, MusicHot

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class MusicHotSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicHot
        fields = '__all__'