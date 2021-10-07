# Generated by Django 3.2.4 on 2021-08-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_remove_student_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='room_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
