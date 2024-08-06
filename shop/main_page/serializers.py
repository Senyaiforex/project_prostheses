from rest_framework import serializers
from main_page.models import *


class TextSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для текста
    """

    class Meta:
        model = TextContent
        fields = ['position', 'title', 'data', 'tag_dev']


class ButtonSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для контента кнопок
    """

    class Meta:
        model = ButtonContent
        fields = ['data', 'image']


class HeaderSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для контента заголовков
    """

    class Meta:
        model = HeaderContent
        fields = ['position', 'type', 'data', 'tag_dev']


class ImageSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для изображений
    """

    class Meta:
        model = ImageContent
        fields = ['position', 'data', 'tag_dev']


class PlaceHolderSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для плейсхолдеров
    """

    class Meta:
        model = PlaceHolder
        fields = ['text']


class FormSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для форм
    """
    placeholders = PlaceHolderSerializer(many=True, read_only=True)

    class Meta:
        model = FormContent
        fields = ['title', 'button', 'accept', 'placeholders']


class FieldContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldContent
        fields = ['field_1', 'field_2', 'field_3', 'image']


class ListRelatedSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для связанных списков
    """
    fields = FieldContentSerializer(many=True, read_only=True)

    class Meta:
        model = ListRelatedContent
        fields = ['tag_dev', 'fields']


class SectionSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для секций
    """

    class Meta:
        model = Section
        fields = ['position', 'page', 'title']
