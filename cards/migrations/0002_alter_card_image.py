# Generated by Django 5.1.1 on 2024-09-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(help_text='Image size 800 x 800 only', upload_to='cards'),
        ),
    ]
