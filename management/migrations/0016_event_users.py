# Generated by Django 4.1.2 on 2022-12-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_event_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(related_name='events', to='management.user'),
        ),
    ]