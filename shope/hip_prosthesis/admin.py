from django.contrib import admin
from .models import *
from coreapp.admin_mixins import *

admin.AdminSite.site_header = 'Администрирование Море Протезов'


class TextContentInline(admin.TabularInline, TextMixin):
    model = HipTextContent


class ImageContentInline(admin.TabularInline, ImageMixin):
    model = HipImageContent


class HeaderContentInline(admin.TabularInline, HeaderMixin):
    model = HipHeaderContent


class ButtonContentInline(admin.TabularInline, ButtonMixin):
    model = HipButtonContent


@admin.register(HipSection)
class SectionAdmin(admin.ModelAdmin, SectionMixin):
    inlines = [TextContentInline, ImageContentInline, HeaderContentInline, ButtonContentInline]
