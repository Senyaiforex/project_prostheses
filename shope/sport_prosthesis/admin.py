from django.contrib import admin
from .models import *
from coreapp.admin_mixins import *

admin.AdminSite.site_header = 'Администрирование Море Протезов'


class TextContentInline(admin.TabularInline, TextMixin):
    model = SportTextContent


class ImageContentInline(admin.TabularInline, ImageMixin):
    model = SportImageContent


class HeaderContentInline(admin.TabularInline, HeaderMixin):
    model = SportHeaderContent


class ButtonContentInline(admin.TabularInline, ButtonMixin):
    model = SportButtonContent


@admin.register(SportSection)
class SectionAdmin(admin.ModelAdmin, SectionMixin):
    inlines = [TextContentInline, ImageContentInline, HeaderContentInline, ButtonContentInline]