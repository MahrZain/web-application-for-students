# Generated by Django 5.1.1 on 2024-09-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_alter_card_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
