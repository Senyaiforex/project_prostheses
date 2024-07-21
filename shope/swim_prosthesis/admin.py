from django.contrib import admin
from .models import *
from coreapp.admin_mixins import *

admin.AdminSite.site_header = 'Администрирование Море Протезов'


class TextContentInline(admin.TabularInline, TextMixin):
    model = SwimTextContent


class ImageContentInline(admin.TabularInline, ImageMixin):
    model = SwimImageContent


class HeaderContentInline(admin.TabularInline, HeaderMixin):
    model = SwimHeaderContent


class ButtonContentInline(admin.TabularInline, ButtonMixin):
    model = SwimButtonContent


@admin.register(SwimSection)
class SectionAdmin(admin.ModelAdmin, SectionMixin):
    inlines = [TextContentInline, ImageContentInline, HeaderContentInline, ButtonContentInline]
