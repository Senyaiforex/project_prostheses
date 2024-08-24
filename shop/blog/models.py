from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from transliterate import translit


class Tag(models.Model):
    """
    Класс-модель для тегов
    """
    name = models.CharField(verbose_name='Название тега', max_length=20, unique=True)
    dec_tag = models.CharField(verbose_name='Декларированный тег', max_length=15, default=' ')

    def __str__(self):
        return self.name if self.name else ' '

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Blog(models.Model):
    """
    Класс-модель для блогов
    """
    title = models.CharField(verbose_name='Название статьи', max_length=200)
    sub_title = models.TextField(verbose_name='Краткое описание статьи')
    content = models.TextField(verbose_name='Содержание статьи')
    image = models.ImageField(upload_to='blog_images/', blank=True, verbose_name='Изображение')
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING,
                            related_name='blogs',
                            verbose_name='Тег',
                            blank=True,
                            null=True)
    slug = models.SlugField(null=True, max_length=255, db_index=True, verbose_name='Слаг', blank=True)

    def __str__(self):
        return self.title if self.title else ' '

    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'Статьи'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="90" height="90" />')
        return "Отсутствует"

    def save(self, *args, **kwargs):
        transliterated_title = translit(self.title, 'ru', reversed=True)
        generated_slug = slugify(transliterated_title, allow_unicode=True)
        self.slug = generated_slug
        try:
            old_image = None
            blog = Blog.objects.filter(id=self.id).first()
            if all((blog, blog.image, blog.image != self.image)):
                old_image = blog.image
        except Exception as ex:
            pass
        super(Blog, self).save(*args, **kwargs)
        if old_image:  # Удалить старое изображение
            old_image.delete(save=False)

    image_tag.short_description = 'Изображение'
