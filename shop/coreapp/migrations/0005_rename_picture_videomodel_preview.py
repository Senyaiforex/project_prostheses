# Generated by Django 5.0.7 on 2024-08-27 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_videomodel_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videomodel',
            old_name='picture',
            new_name='preview',
        ),
    ]
