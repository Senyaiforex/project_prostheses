# Generated by Django 5.0.7 on 2024-08-03 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0009_alter_buttoncontent_tag_dev_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formcontent',
            options={'verbose_name': 'экземпляр формы', 'verbose_name_plural': 'Формы'},
        ),
    ]
