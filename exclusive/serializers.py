from rest_framework import serializers
from .models import ExclusiveItem

class ExclusiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExclusiveItem
        fields = '__all__'
