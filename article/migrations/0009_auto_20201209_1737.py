# Generated by Django 2.2 on 2020-12-09 09:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_articlepost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]