# Generated by Django 3.2.4 on 2021-08-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210808_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_birth',
        ),
    ]
