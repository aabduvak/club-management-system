# Generated by Django 4.1.2 on 2022-12-21 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='surname',
            new_name='last_name',
        ),
    ]
