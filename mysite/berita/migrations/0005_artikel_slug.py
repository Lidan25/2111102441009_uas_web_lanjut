# Generated by Django 5.0.2 on 2024-06-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0004_artikel_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
