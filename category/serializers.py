from rest_framework import serializers
from .models import Ballad, Category, Rock, Edm,  Viet, Hiprap

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BalladSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ballad
        fields = '__all__'

class RockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rock
        fields = '__all__'

class EdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edm
        fields = '__all__'

class VietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viet
        fields = '__all__'

class HiprapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiprap
        fields = '__all__'