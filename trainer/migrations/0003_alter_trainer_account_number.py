# Generated by Django 3.2.4 on 2021-08-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_auto_20210812_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='account_number',
            field=models.CharField(default=None, max_length=10),
        ),
    ]