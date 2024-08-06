from rest_framework import serializers
from blog.models import *


class TagSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')
    tag = serializers.CharField(source='dec_tag')

    class Meta:
        model = Tag
        fields = ['title', 'tag']


class BlogSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = Blog
        fields = ['title', 'sub_title', 'content', 'image', 'tag']
