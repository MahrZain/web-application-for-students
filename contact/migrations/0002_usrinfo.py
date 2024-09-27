# Generated by Django 5.1.1 on 2024-09-10 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usrinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('map_link', models.URLField()),
            ],
        ),
    ]