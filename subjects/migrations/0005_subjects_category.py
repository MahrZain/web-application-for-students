# Generated by Django 5.1.1 on 2024-09-08 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('subjects', '0004_subjects_class_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
