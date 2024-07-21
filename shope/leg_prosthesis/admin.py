from django.contrib import admin
from .models import *
from coreapp.admin_mixins import *

admin.AdminSite.site_header = 'Администрирование Море Протезов'


class TextContentInline(admin.TabularInline, TextMixin):
    model = LegTextContent


class ImageContentInline(admin.TabularInline, ImageMixin):
    model = LegImageContent


class HeaderContentInline(admin.TabularInline, HeaderMixin):
    model = LegHeaderContent


class ButtonContentInline(admin.TabularInline, ButtonMixin):
    model = LegButtonContent


@admin.register(LegSection)
class SectionAdmin(admin.ModelAdmin, SectionMixin):
    inlines = [TextContentInline, ImageContentInline, HeaderContentInline, ButtonContentInline]
