import nested_admin
from django.contrib import admin
from .models import SpecialistModel


@admin.register(SpecialistModel)
class TagAdmin(nested_admin.NestedModelAdmin):
    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
