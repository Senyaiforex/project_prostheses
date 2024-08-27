from rest_framework import serializers
from .models import SpecialistModel, VideoModel, CategoryModel


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('title', 'dec_tag')


class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = VideoModel
        fields = ('title',
                  'description', 'category',
                  'video', 'preview', 'tag_dev')
