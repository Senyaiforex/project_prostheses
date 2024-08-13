from rest_framework import serializers
from main_page.models import *
import re


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
        fields = ['field_1', 'field_2', 'image']


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
    type = serializers.SerializerMethodField()

    class Meta:
        model = PlaceHolder
        fields = ['text', 'type']

    def get_type(self, obj):
        # Регулярное выражение для проверки номера телефона
        phone_regex = re.compile(r'^(?:\+7|8|9)\d{9,10}$')
        list_text_tel = ['телефон', 'номер телефона', 'телефонный номер', 'номер',
                         'телефон для связи', 'ваш телефон']
        list_text_email = ['email', 'электронная почта', 'email адрес', 'электронный адрес']
        email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if obj.text and (phone_regex.match(obj.text) or obj.text.lower() in list_text_tel):
            return 'tel'
        elif obj.text and (obj.text.lower() in list_text_email or email_regex.match(obj.text)):
            return 'email'
        else:
            return 'text'


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
