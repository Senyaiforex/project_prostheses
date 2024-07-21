from coreapp.models import *


class LegSection(AbstractSection):
    """
    Модель для секции сайта в пределах одной страницы
    """


class SectionMixin(models.Model):
    section = models.ForeignKey(
            LegSection,
            on_delete=models.CASCADE,
            verbose_name='Секция'
    )

    class Meta:
        abstract = True


class LegTextContent(AbstractTextContent, SectionMixin):
    """
    Модель для текстового контента в пределах одной секции
    """


class LegButtonContent(AbstractButtonContent, SectionMixin):
    """
    Модель для кнопок в пределах одной секции
    """


class LegHeaderContent(AbstractHeaderContent, SectionMixin):
    """
    Модель для заголовков в пределах одной секции
    """


class LegImageContent(AbstractImageContent, SectionMixin):
    """
    Модель для картинок в пределах одной секции
    """
