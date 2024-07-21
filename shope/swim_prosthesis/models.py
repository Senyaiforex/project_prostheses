from coreapp.models import *


class SwimSection(AbstractSection):
    """
    Модель для секции сайта в пределах одной страницы
    """


class SectionMixin(models.Model):
    section = models.ForeignKey(
            SwimSection,
            on_delete=models.CASCADE,
            verbose_name='Секция'
    )

    class Meta:
        abstract = True


class SwimTextContent(AbstractTextContent, SectionMixin):
    """
    Модель для текстового контента в пределах одной секции
    """


class SwimButtonContent(AbstractButtonContent, SectionMixin):
    """
    Модель для кнопок в пределах одной секции
    """


class SwimHeaderContent(AbstractHeaderContent, SectionMixin):
    """
    Модель для заголовков в пределах одной секции
    """


class SwimImageContent(AbstractImageContent, SectionMixin):
    """
    Модель для картинок в пределах одной секции
    """
