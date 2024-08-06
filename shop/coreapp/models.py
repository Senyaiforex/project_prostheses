from django.db import models
from django.utils.html import mark_safe
from ordered_model.models import OrderedModel


# Create your models here.

class AbstractSection(models.Model):
    """
    Модель для секции сайта в пределах одной страницы
    """
    PAGES = [
            ('hip', 'Протез бедра'),
            ('leg', 'Протез голени'),
            ('arm', 'Протез руки'),
            ('sport', 'Протез спортивный'),
            ('swim', 'Протез купальный'),
            ('main', 'Главная'),
            ('about', 'О компании'),
            ('interview', 'Интервью с клиентами'),
            ('contacts', 'Контакты')
    ]
    title = models.CharField(verbose_name='Название секции',
                             max_length=100,
                             default=' ')
    description = models.CharField(verbose_name='Описание секции(можно оставить пустым)',
                                   max_length=120, blank=True,
                                   default=' ')
    page = models.CharField(
            max_length=30,
            choices=PAGES,
            verbose_name='Страница',
            null=True)
    position = models.IntegerField(editable=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.position is None:  # Заполняем поле только если оно пустое
            self.position = self._generate_fgr_value()
        else:
            pass
        super().save(*args, **kwargs)

    #
    #
    def _generate_fgr_value(self):
        # Логика для генерации значения для textcontent
        last_instance = self.__class__.objects.order_by('-position').first()
        if last_instance:
            return last_instance.position + 1
        return 1


class AbstractTextContent(models.Model):
    """
    Модель для текстового контента в пределах одной секции
    """
    title = models.CharField(verbose_name='Общая информация о тексте',
                             max_length=60, blank=True, null=True)
    data = models.TextField(verbose_name='Содержание текста',
                            null=True,
                            blank=True)
    position = models.IntegerField(editable=True, blank=True, null=True)

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
                             max_length=60,
                             blank=True,
                             null=True,
                             default=' ')
    data = models.TextField(verbose_name='Текст кнопки', null=True,
                            blank=True)
    position = models.IntegerField(editable=True, blank=True, null=True)
    image = models.ImageField(upload_to='button_images/', verbose_name='Изображение для кнопки',
                              null=True,
                              blank=True)

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'
        abstract = True

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="90" height="90" />')
        return "Отсутствует"

    image_tag.short_description = 'Изображение'


class AbstractHeaderContent(models.Model):
    """
    Модель для заголовков в пределах одной секции
    """
    title = models.CharField(verbose_name='Общая информация о содержании заголовка',
                             max_length=40, blank=True, null=True)
    type = models.CharField(verbose_name='Тип заголовка(h1, h2, h3, h4, h5)',
                            max_length=20, blank=True, null=True)
    data = models.TextField(verbose_name='Текст заголовка',
                            blank=True, null=True)
    position = models.IntegerField(editable=True, blank=True, null=True)

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
                             max_length=50, blank=True, null=True)

    data = models.ImageField(upload_to='page_images/', verbose_name='Изображение', blank=True, null=True)
    position = models.IntegerField(editable=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        abstract = True

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.data:
            return mark_safe(f'<img src="{self.data.url}" width="90" height="90" />')
        return "Отсутствует"

    image_tag.short_description = 'Изображение'


class SpecialistModel(models.Model):
    """
    Модель для специалистов сайта
    """
    full_name = models.CharField(verbose_name='Фамилия Имя Отчество', max_length=90)
    photo = models.ImageField(upload_to='specialists/', verbose_name='Фотография')
    job_title = models.CharField(verbose_name='Должность', max_length=100)
    bio = models.TextField(verbose_name='Биография')

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return self.full_name
