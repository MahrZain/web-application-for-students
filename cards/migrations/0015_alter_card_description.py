# Generated by Django 5.1.1 on 2024-09-26 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0014_alter_card_description_alter_card_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(help_text='must be 75 characters', max_length=75, null=True),
        ),
    ]