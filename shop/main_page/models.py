from coreapp.models import *
from django.db import models
import requests
import json
from django.conf import settings
url_notification = settings.URL_NOTIFICATION

def send_notification():
    try:
        msg = {'revalidate': True}
        requests.post(url_notification, data=json.dumps(msg))
    except requests.exceptions.RequestException as e:
        pass


class Section(AbstractSection):
    """
    Модель для секции сайта в пределах одной страницы
    """


class SectionMixin(models.Model):
    section = models.ForeignKey(
            Section,
            on_delete=models.CASCADE,
            verbose_name='Секция'
    )
    tag_dev = models.CharField(max_length=30, verbose_name='Тэг', blank=True, null=True)

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

    class Meta:
        abstract = True


class TextContent(AbstractTextContent, SectionMixin):
    """
    Модель для текстового контента в пределах одной секции
    """


class ButtonContent(AbstractButtonContent, SectionMixin):
    """
    Модель для кнопок в пределах одной секции
    """

    def save(self, *args, **kwargs):
        try:
            old_image = None
            button = ButtonContent.objects.filter(id=self.id).first()
            if all((button.image, button.image, button.image != self.image)):
                old_image = button.image
        except Exception as ex:
            pass
        super(ButtonContent, self).save(*args, **kwargs)
        if old_image:  # Удалить старое изображение
            old_image.delete(save=False)


class HeaderContent(AbstractHeaderContent, SectionMixin):
    """
    Модель для заголовков в пределах одной секции
    """


class ImageContent(AbstractImageContent, SectionMixin):
    """
    Модель для картинок в пределах одной секции
    """

    def save(self, *args, **kwargs):
        try:
            old_image = None
            image = ImageContent.objects.filter(id=self.id).first()
            if all((image, image.data, image.data != self.data)):
                old_image = image.data
        except Exception as ex:
            pass
        super(ImageContent, self).save(*args, **kwargs)
        if old_image:  # Удалить старое изображение
            old_image.delete(save=False)


class ListRelatedContent(SectionMixin):
    """
    Модель для связанных списков в одной секции
    """
    description = models.CharField(verbose_name='Описание связанного списка', max_length=70)
    position = models.IntegerField(editable=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Связанный список'
        verbose_name_plural = 'Связанные списки'

    def __str__(self):
        return self.description[:30] if self.description else ' '


class FieldContent(models.Model):
    list_related = models.ForeignKey(ListRelatedContent,
                                     on_delete=models.CASCADE,
                                     verbose_name='Связанный список',
                                     related_name='fields'
                                     )
    field_1 = models.CharField(verbose_name='поле 1', max_length=2000, blank=True, null=True)
    field_2 = models.TextField(verbose_name='поле 2', max_length=2000, blank=True, null=True)
    field_3 = models.TextField(verbose_name='поле 3', max_length=5000, blank=True, null=True)
    position = models.IntegerField(editable=True, blank=True, null=True)
    image = models.ImageField(upload_to='relationlist_images/', verbose_name='Изображение',
                              null=True,
                              blank=True)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="80" height="80" />')
        return "Отсутствует"

    image_tag.short_description = 'Изображение'

    def save(self, *args, **kwargs):
        if self.position is None:  # Заполняем поле только если оно пустое
            self.position = self._generate_fgr_value()
        else:
            pass
        try:
            old_image = None
            field = FieldContent.objects.filter(id=self.id).first()
            if all((field, field.image, field.image != self.image)):
                old_image = field.image
        except Exception as ex:
            pass
        super().save(*args, **kwargs)
        send_notification()
        if old_image:  # Удалить старое изображение
            old_image.delete(save=False)

    #
    #
    def _generate_fgr_value(self):
        # Логика для генерации значения для textcontent
        last_instance = self.__class__.objects.order_by('-position').first()
        if last_instance:
            return last_instance.position + 1
        return 1

    class Meta:
        verbose_name = 'элемент'
        verbose_name_plural = 'элементы'

    def __str__(self):
        return 'элемент списка'


class FormContent(SectionMixin):
    position = models.IntegerField(editable=True, blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name='Описание', blank=True, null=True)
    button = models.CharField(max_length=30, verbose_name='Кнопка', blank=True, null=True)
    accept = models.CharField(max_length=200, verbose_name='Согласие на отправку формы', blank=True, null=True)

    class Meta:
        verbose_name = 'экземпляр формы'
        verbose_name_plural = 'Формы'

    def __str__(self):
        return self.title if self.title else ' '


class PlaceHolder(models.Model):
    position = models.IntegerField(editable=True, blank=True, null=True)
    text = models.CharField(max_length=30, verbose_name='текст', blank=True, null=True)
    form = models.ForeignKey(FormContent,
                             on_delete=models.CASCADE,
                             verbose_name='Форма',
                             related_name='placeholders'
                             )

    def __str__(self):
        return self.text if self.text else ' '

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

    class Meta:
        verbose_name = 'экземпляр поля'
        verbose_name_plural = 'Поля формы'


class Page(Section):
    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Главная'


class AboutPage(Section):
    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'О компании'


class HipPage(Section):
    """
    Модель протеза бедра
    """

    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Протез бедра'


class LegPage(Section):
    """
    Модель протеза голени
    """

    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Протез голени'


class ArmPage(Section):
    """
    Модель протеза руки
    """

    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Протез руки'


class SportPage(Section):
    """
    Модель спортивного протеза
    """

    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Протез спортивный'


class SwimPage(Section):
    """
    Модель купального протеза
    """

    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Протез купальный'


class ContactPage(Section):
    """
    Модель страницы контактов
    """

    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Контакты'


class FooterPage(Section):
    """
    Модель страницы футера
    """

    class Meta:
        proxy = True
        verbose_name = 'Секция'
        verbose_name_plural = 'Футер'
