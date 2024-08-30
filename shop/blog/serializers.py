from rest_framework import serializers
from blog.models import *
from django.conf import settings


class TagSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='name')
    tag = serializers.CharField(source='dec_tag')

    class Meta:
        model = Tag
        fields = ['title', 'tag']


class BlogSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['title', 'sub_title', 'content', 'image', 'tag', 'url']

    def get_url(self, obj):
        # request = self.context.get('request')
        # domain = request.build_absolute_uri('/') if request else settings.DEFAULT_DOMAIN
        return obj.slug

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Если множество объектов сериализуется, просто удалите поле 'text_rich'
        if self.context['many']:  # or some other logic to determine many=True
            representation.pop('content', None)

        return representation
