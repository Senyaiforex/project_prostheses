from coreapp.models import *
from django.db import models


class MainSection(AbstractSection):
    """
    Модель для секции сайта в пределах одной страницы
    """


class SectionMixin(models.Model):
    section = models.ForeignKey(
            MainSection,
            on_delete=models.CASCADE,
            verbose_name='Секция'
    )

    class Meta:
        abstract = True


class MainTextContent(AbstractTextContent, SectionMixin):
    """
    Модель для текстового контента в пределах одной секции
    """


class MainButtonContent(AbstractButtonContent, SectionMixin):
    """
    Модель для кнопок в пределах одной секции
    """


class MainHeaderContent(AbstractHeaderContent, SectionMixin):
    """
    Модель для заголовков в пределах одной секции
    """


class MainImageContent(AbstractImageContent, SectionMixin):
    """
    Модель для картинок в пределах одной секции
    """
