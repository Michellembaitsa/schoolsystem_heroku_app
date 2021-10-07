# Generated by Django 3.2.4 on 2021-09-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0003_auto_20210820_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendars',
            name='attendees',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='event_duration',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='event_goal',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='organizer',
        ),
        migrations.RemoveField(
            model_name='calendars',
            name='venue',
        ),
        migrations.AddField(
            model_name='calendars',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calendars',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='calendars',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]