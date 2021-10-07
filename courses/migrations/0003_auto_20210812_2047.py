# Generated by Django 3.2.4 on 2021-08-12 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_courses_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_description',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='courses',
            name='duration_of_lesson',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_code',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_trainer',
            field=models.CharField(default=None, max_length=10),
        ),
    ]