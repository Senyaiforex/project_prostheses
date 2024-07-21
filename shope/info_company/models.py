from coreapp.models import *


class InfoSection(AbstractSection):
    """
    Модель для секции сайта в пределах одной страницы
    """


class SectionMixin(models.Model):
    section = models.ForeignKey(
            InfoSection,
            on_delete=models.CASCADE,
            verbose_name='Секция'
    )

    class Meta:
        abstract = True


class InfoTextContent(AbstractTextContent, SectionMixin):
    """
    Модель для текстового контента в пределах одной секции
    """


class InfoButtonContent(AbstractButtonContent, SectionMixin):
    """
    Модель для кнопок в пределах одной секции
    """


class InfoHeaderContent(AbstractHeaderContent, SectionMixin):
    """
    Модель для заголовков в пределах одной секции
    """


class InfoImageContent(AbstractImageContent, SectionMixin):
    """
    Модель для картинок в пределах одной секции
    """
