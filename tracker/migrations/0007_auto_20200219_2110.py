# Generated by Django 3.0.3 on 2020-02-19 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_remove_match_deck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='player',
        ),
        migrations.DeleteModel(
            name='League',
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]