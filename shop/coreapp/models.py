from django.db import models
from django.utils.html import mark_safe
from ordered_model.models import OrderedModel
from django.core.validators import FileExtensionValidator
import requests


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
            ('contacts', 'Контакты'),
            ('footer', 'Футер')
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
        return self.title if self.title else ' '

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
        return self.title if self.title else ' '


class AbstractButtonContent(models.Model):
    """
    Модель для кнопок в пределах одной секции
    """
    title = models.CharField(verbose_name='Общая информация о содержании кнопки',
                             max_length=60,
                             blank=True,
                             null=True,
                             default=' ')
    field_1 = models.CharField(verbose_name='Текст кнопки', null=True, max_length=70,
                               blank=True)
    field_2 = models.CharField(verbose_name='Текст кнопки', null=True, default=None, max_length=70,
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
        return self.title if self.title else ' '

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
        return self.title if self.title else ' '


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
        return self.title if self.title else ' '

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
        verbose_name = 'специалиста'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return self.full_name if self.full_name else ' '

    def image_tag(self):
        if self.photo:
            return mark_safe(f'<img src="{self.image.url}" width="90" height="90" />')
        return "Отсутствует"

    image_tag.short_description = 'Фото'


class CategoryModel(models.Model):
    """
    Модель для категорий видео
    """
    title = models.CharField(verbose_name='Название категории', max_length=50)
    dec_tag = models.CharField(verbose_name='Декларированный тег', max_length=20)

    def __str__(self):
        return self.title if self.title else ' '

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории видео'


class VideoModel(models.Model):
    """
    Модель для видео сайта
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
    ]
    page = models.CharField(
            max_length=30,
            choices=PAGES,
            verbose_name='Страница',
            null=True,
            blank=True)
    title = models.CharField(verbose_name='Название видео', max_length=100)
    description = models.TextField(verbose_name='Описание видео')
    video = models.FileField(upload_to='videos/',
                             verbose_name='Видеофайл',
                             validators=[FileExtensionValidator(
                                     allowed_extensions=['mp4', 'avi', 'webm', 'mov', 'html5', 'webm'],
                                     message='Допустимые форматы: mp4, avi, webm, mov, html5, webm')])
    preview = models.ImageField(upload_to='video_images/', verbose_name='Превью видео')
    tag_dev = models.CharField(verbose_name='Тег для разработки', max_length=20)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='Категория видео')

    def __str__(self):
        return self.title if self.title else ' '

    def save(self, *args, **kwargs):
        try:
            old_picture = None
            old_video = None
            video = VideoModel.objects.filter(id=self.id).first()
            if all((video, video.video, video.video != self.video)):
                old_video = video.video
            if all((video, video.picture, video.picture != self.picture)):
                old_picture = video.picture
        except Exception as ex:
            pass
        super(VideoModel, self).save(*args, **kwargs)
        if old_video:
            old_video.delete(save=False)
        if old_picture:
            old_picture.delete(save=False)

    def video_tag(self):
        if self.video:
            poster_url = self.preview.url if self.preview else ""
            return mark_safe(
                    f'<video width="320" height="240" controls poster="{poster_url}">'
                    f'<source src="{self.video.url}" type="video/mp4">'
                    f''
                    f'</video>')
        return "Отсутствует"

    video_tag.short_description = 'Видео'

    class Meta:
        verbose_name = 'видео'
        verbose_name_plural = 'Видео'
