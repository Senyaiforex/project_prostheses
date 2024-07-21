from django.db import models
from django.utils.html import mark_safe
from coreapp.models import *


class HipSection(AbstractSection):
    """
    Модель для секции сайта в пределах одной страницы
    """


class SectionMixin(models.Model):
    section = models.ForeignKey(
            HipSection,
            on_delete=models.CASCADE,
            verbose_name='Секция'
    )

    class Meta:
        abstract = True


class HipTextContent(AbstractTextContent, SectionMixin):
    """
    Модель для текстового контента в пределах одной секции
    """


class HipButtonContent(AbstractButtonContent, SectionMixin):
    """
    Модель для кнопок в пределах одной секции
    """


class HipHeaderContent(AbstractHeaderContent, SectionMixin):
    """
    Модель для заголовков в пределах одной секции
    """


class HipImageContent(AbstractImageContent, SectionMixin):
    """
    Модель для картинок в пределах одной секции
    """
