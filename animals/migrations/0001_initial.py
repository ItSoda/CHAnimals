# Generated by Django 4.2 on 2023-11-23 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('species', models.CharField(max_length=200, verbose_name='Порода')),
                ('age', models.PositiveIntegerField(default=0)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'животное',
                'verbose_name_plural': 'Животные',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='all_images')),
            ],
            options={
                'verbose_name': 'Фотографию',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='FormAnimals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animals')),
            ],
            options={
                'verbose_name': 'Заявку',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
