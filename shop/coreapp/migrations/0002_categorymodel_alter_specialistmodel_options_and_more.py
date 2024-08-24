# Generated by Django 5.0.7 on 2024-08-24 13:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
                ('dec_tag', models.CharField(max_length=20, verbose_name='Декларированный тег')),
            ],
            options={
                'verbose_name': 'Категория видео',
                'verbose_name_plural': 'Категории видео',
            },
        ),
        migrations.AlterModelOptions(
            name='specialistmodel',
            options={'verbose_name': 'специалиста', 'verbose_name_plural': 'Специалисты'},
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название видео')),
                ('description', models.TextField(verbose_name='Описание видео')),
                ('video', models.FileField(upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'webm', 'mov', 'html5', 'webm'], message='Допустимые форматы: mp4, avi, webm, mov, html5, webm')], verbose_name='Видеофайл')),
                ('picture', models.ImageField(upload_to='video_images/', verbose_name='Превью видео')),
                ('tag_dev', models.CharField(max_length=20, verbose_name='Тег для разработки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.categorymodel', verbose_name='Категория видео')),
            ],
            options={
                'verbose_name': 'видео',
                'verbose_name_plural': 'Видео',
            },
        ),
    ]
