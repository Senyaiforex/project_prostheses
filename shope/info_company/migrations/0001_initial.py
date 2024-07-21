# Generated by Django 5.0.7 on 2024-07-20 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=70, verbose_name='Название секции')),
                ('description', models.CharField(blank=True, default=' ', max_length=120, verbose_name='Описание секции(можно оставить пустым)')),
            ],
            options={
                'verbose_name': 'Секция',
                'verbose_name_plural': 'Секции',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfoImageContent',
            fields=[
                ('position', models.IntegerField(auto_created=True, blank=True, db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=' ', max_length=50, verbose_name='Общая информация о содержании картинки')),
                ('data', models.ImageField(upload_to='page_images/', verbose_name='Изображение')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_company.infosection', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfoHeaderContent',
            fields=[
                ('position', models.IntegerField(auto_created=True, blank=True, db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=' ', max_length=40, verbose_name='Общая информация о содержании заголовка')),
                ('type', models.CharField(blank=True, default=' ', max_length=20, verbose_name='Тип заголовка(h1, h2, h3, h4, h5)')),
                ('data', models.TextField(blank=True, default=' ', verbose_name='Текст заголовка')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_company.infosection', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовки',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfoButtonContent',
            fields=[
                ('position', models.IntegerField(auto_created=True, blank=True, db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=' ', max_length=60, verbose_name='Общая информация о содержании кнопки')),
                ('data', models.TextField(blank=True, default=' ', verbose_name='Текст кнопки')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_company.infosection', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Кнопка',
                'verbose_name_plural': 'Кнопки',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InfoTextContent',
            fields=[
                ('position', models.IntegerField(auto_created=True, blank=True, db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default=' ', max_length=60, verbose_name='Общая информация о тексте')),
                ('data', models.TextField(blank=True, default=' ', verbose_name='Содержание текста')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_company.infosection', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Текстовый контент',
                'verbose_name_plural': 'Текстовый контент',
                'abstract': False,
            },
        ),
    ]
