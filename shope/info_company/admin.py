from django.contrib import admin
from .models import *
from coreapp.admin_mixins import *

admin.AdminSite.site_header = 'Администрирование Море Протезов'


class TextContentInline(admin.TabularInline, TextMixin):
    model = InfoTextContent


class ImageContentInline(admin.TabularInline, ImageMixin):
    model = InfoImageContent


class HeaderContentInline(admin.TabularInline, HeaderMixin):
    model = InfoHeaderContent


class ButtonContentInline(admin.TabularInline, ButtonMixin):
    model = InfoButtonContent


@admin.register(InfoSection)
class SectionAdmin(admin.ModelAdmin, SectionMixin):
    inlines = [TextContentInline, ImageContentInline, HeaderContentInline, ButtonContentInline]
