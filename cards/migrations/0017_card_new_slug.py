# Generated by Django 5.1.1 on 2024-09-26 06:13

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0016_alter_card_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]