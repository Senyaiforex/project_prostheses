from django.db import models
from django.utils.html import mark_safe


class Tag(models.Model):
    """
    Класс-модель для тегов
    """
    name = models.CharField(verbose_name='Название тега', max_length=20, unique=True)
    dec_tag = models.CharField(verbose_name='Декларированный тег', max_length=15, default=' ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Blog(models.Model):
    """
    Класс-модель для блогов
    """
    title = models.CharField(verbose_name='Название блога', max_length=200)
    sub_title = models.CharField(verbose_name='Краткое описание блога', max_length=200)
    content = models.TextField(verbose_name='Содержание блога')
    image = models.ImageField(upload_to='blog_images/', blank=True, verbose_name='Изображение')
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING,
                            related_name='blogs',
                            verbose_name='Тег',
                            blank=True,
                            null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="90" height="90" />')
        return "Отсутствует"

    image_tag.short_description = 'Изображение'
