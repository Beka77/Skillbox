# Generated by Django 4.1.1 on 2022-10-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, verbose_name='Человекопонятный URL'),
            preserve_default=False,
        ),
    ]