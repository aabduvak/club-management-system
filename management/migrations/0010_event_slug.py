# Generated by Django 4.1.2 on 2022-12-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_remove_club_events_event_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]