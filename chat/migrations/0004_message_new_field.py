# Generated by Django 4.2 on 2023-12-24 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_personalmessage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='new_field',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
