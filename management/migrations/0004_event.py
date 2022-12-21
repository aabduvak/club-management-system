# Generated by Django 4.1.2 on 2022-12-19 00:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_role_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_desc', models.CharField(max_length=400)),
                ('long_desc', models.TextField()),
                ('img', models.ImageField(upload_to='posts')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
