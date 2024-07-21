from django.db import models
from django.utils.html import mark_safe


# Create your models here.

class AbstractSection(models.Model):
    """
    Модель для секции сайта в пределах одной страницы
    """
    title = models.CharField(verbose_name='Название секции',
                             max_length=70,
                             default=' ')
    description = models.CharField(verbose_name='Описание секции(можно оставить пустым)',
                                   max_length=120, blank=True,
                                   default=' ')

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'
        abstract = True

    def __str__(self):
        return self.title


class AbstractTextContent(models.Model):
    """
    Модель для текстового контента в пределах одной секции
    """
    title = models.CharField(verbose_name='Общая информация о тексте',
                             max_length=60, blank=True,
                             default=' ')
    data = models.TextField(verbose_name='Содержание текста',
                            blank=True, default=' ')
    position = models.IntegerField(primary_key=True, editable=True, blank=True, db_index=True)  # после разработки удалить это поле

    class Meta:
        verbose_name = 'Текстовый контент'
        verbose_name_plural = 'Текстовый контент'
        abstract = True

    def __str__(self):
        return self.title


class AbstractButtonContent(models.Model):
    """
    Модель для кнопок в пределах одной секции
    """
    title = models.CharField(verbose_name='Общая информация о содержании кнопки',
                             max_length=60, blank=True,
                             default=' ')
    data = models.TextField(verbose_name='Текст кнопки',
                            blank=True, default=' ')
    position = models.IntegerField(primary_key=True, editable=True, blank=True, db_index=True)  # после разработки удалить это поле

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'
        abstract = True

    def __str__(self):
        return self.title


class AbstractHeaderContent(models.Model):
    """
    Модель для заголовков в пределах одной секции
    """
    title = models.CharField(verbose_name='Общая информация о содержании заголовка',
                             max_length=40, blank=True,
                             default=' ')
    type = models.CharField(verbose_name='Тип заголовка(h1, h2, h3, h4, h5)',
                            max_length=20, blank=True,
                            default=' ')
    data = models.TextField(verbose_name='Текст заголовка',
                            blank=True, default=' ')
    position = models.IntegerField(primary_key=True, editable=True, blank=True, db_index=True)  # после разработки удалить это поле

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'
        abstract = True

    def __str__(self):
        return self.title


class AbstractImageContent(models.Model):
    """
    Модель для картинок в пределах одной секции
    """
    title = models.CharField(verbose_name='Общая информация о содержании картинки',
                             max_length=50, blank=True,
                             default=' ')

    data = models.ImageField(upload_to='page_images/', verbose_name='Изображение')
    position = models.IntegerField(primary_key=True, editable=True, blank=True, db_index=True)  # после разработки удалить это поле

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        abstract = True

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.data:
            return mark_safe(f'<img src="{self.data.url}" width="90" height="90" />')
        return "No Image"

    image_tag.short_description = 'Изображение'
