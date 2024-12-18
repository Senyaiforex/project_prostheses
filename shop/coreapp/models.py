import os

from django.core.files.base import ContentFile
from django.db import models
from django.utils.html import mark_safe
from moviepy.video.io.VideoFileClip import VideoFileClip
from ordered_model.models import OrderedModel
from django.core.validators import FileExtensionValidator
import requests
import json
from django.conf import settings
from django.utils.text import slugify
from transliterate import translit

# Create your models here.
url_notification = settings.URL_NOTIFICATION


def send_notification():
    try:
        msg = {'revalidate': True}
        requests.post(url_notification, data=json.dumps(msg))
    except requests.exceptions.RequestException as e:
        pass


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
        send_notification()
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
    hidden = models.BooleanField(default=False, verbose_name='Скрытый')
    class Meta:
        verbose_name = 'специалиста'
        verbose_name_plural = 'Специалисты'

    def save(self, *args, **kwargs):
        send_notification()
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        send_notification()
        super(CategoryModel, self).save(*args, **kwargs)

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
    title = models.CharField(verbose_name='Название видео', max_length=100, blank=False, unique=True)
    description = models.TextField(verbose_name='Описание видео')
    video = models.FileField(upload_to='videos/',
                             verbose_name='Видеофайл',
                             validators=[FileExtensionValidator(
                                     allowed_extensions=['mp4', 'avi', 'webm', 'mov', 'html5', 'webm'],
                                     message='Допустимые форматы: mp4, avi, webm, mov, html5, webm')])
    preview = models.ImageField(upload_to='video_images/', verbose_name='Превью видео',
                                blank=True, null=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='url-адрес видео',
                            blank=False, unique=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name='Категория видео')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title if self.title else ' '

    def save(self, *args, **kwargs):
        transliterated_title = translit(self.title, 'ru', reversed=True)
        generated_slug = slugify(transliterated_title, allow_unicode=True)
        self.slug = generated_slug
        try:
            old_picture = None
            old_video = None
            video = VideoModel.objects.filter(id=self.id).first()
            if all((video, video.video, video.video != self.video)):
                old_video = video.video
            if all((video, video.preview, video.preview != self.preview)):
                old_picture = video.preview
            else:
                if not self.preview and self.video:
                    try:
                        # Определяем временной путь для сохранения превью
                        video_clip = VideoFileClip(self.video.path)
                        preview_filename = f'{self.id}_preview.jpg'
                        preview_path = os.path.join('video_images/', preview_filename)
                        video_clip.save_frame(preview_path, t=1)
                        video_clip.close()
                        with open(preview_path, 'rb') as f:
                            content = ContentFile(f.read(), name=preview_filename)
                            self.preview.save(preview_filename, content, save=False)
                        if os.path.exists(preview_path):
                            os.remove(preview_path)
                    except Exception as e:
                        pass
        except Exception as ex:
            pass
        super(VideoModel, self).save(*args, **kwargs)
        send_notification()
        if old_video:
            old_video.delete(save=False)
        if old_picture:
            old_picture.delete(save=False)

    def delete(self, *args, **kwargs):
        preview = self.preview
        video = self.video
        super(VideoModel, self).delete(*args, **kwargs)
        preview.delete(save=False)
        video.delete(save=False)

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
