# Generated by Django 5.1.1 on 2024-09-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='downlaod',
            options={'verbose_name': 'download', 'verbose_name_plural': 'downloads'},
        ),
        migrations.AddField(
            model_name='downlaod',
            name='image',
            field=models.ImageField(null=True, upload_to='download'),
        ),
    ]