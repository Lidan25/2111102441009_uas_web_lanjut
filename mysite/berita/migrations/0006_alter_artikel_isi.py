# Generated by Django 5.0.2 on 2024-06-26 03:31

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0005_artikel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
