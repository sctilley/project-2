# Generated by Django 3.0.3 on 2020-02-18 03:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
