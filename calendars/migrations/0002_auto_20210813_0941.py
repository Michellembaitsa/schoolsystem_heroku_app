# Generated by Django 3.2.4 on 2021-08-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendars',
            name='event_goal',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='event_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='organizer',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='venue',
            field=models.CharField(max_length=10),
        ),
    ]
