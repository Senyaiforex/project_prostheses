from rest_framework import serializers
from .models import SpecialistModel


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistModel
        fields = '__all__'
