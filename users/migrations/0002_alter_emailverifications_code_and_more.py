# Generated by Django 4.2 on 2023-12-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifications',
            name='code',
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='emailverifications',
            name='expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
