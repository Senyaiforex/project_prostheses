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


class VideoTagSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    tag = serializers.CharField(source='dec_tag')

    class Meta:
        model = CategoryModel
        fields = ['title', 'tag']



class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    url = serializers.SerializerMethodField()

    class Meta:
        model = VideoModel
        fields = ('title',
                  'description', 'category',
                  'video', 'preview', 'url')

    def get_url(self, obj):
        return obj.slug
