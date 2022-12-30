# Generated by Django 4.1.2 on 2022-12-30 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='events',
        ),
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clubs', to='management.club'),
        ),
    ]
