# Generated by Django 4.2 on 2023-11-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TG_USER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True, verbose_name='USER ID')),
                ('username', models.CharField(blank=True, max_length=256, null=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
