from main_page.serializers import *
from django.db.models import QuerySet
from .main_section import *


def create_data_dict(position: int,
                     text_content: QuerySet,
                     button_content: QuerySet,
                     image_content: QuerySet,
                     header_content: QuerySet,
                     list_content: QuerySet,
                     form_content: QuerySet):
    """
    Функция, которая принимает на вход номер секции и
    объекты контента и создаёт словарь с данными для секции
    :return: dict
    """
    text_data = TextSerializer(text_content, many=True).data
    button_data = ButtonSerializer(button_content, many=True).data
    image_data = ImageSerializer(image_content, many=True).data
    header_data = HeaderSerializer(header_content, many=True).data
    list_data = ListRelatedSerializer(list_content, many=True).data
    form_data = FormSerializer(form_content, many=True).data
    return main_section(position, text_data, button_data, image_data, header_data, list_data, form_data)


    # func_name = f"{page}_section_{position}"
    # section_function = globals().get(func_name)
    # return section_function(text_data, button_data, image_data, header_data, list_data, form_data)