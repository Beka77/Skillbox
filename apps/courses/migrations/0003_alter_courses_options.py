# Generated by Django 4.1.1 on 2022-10-12 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_currency'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
    ]
