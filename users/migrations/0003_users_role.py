# Generated by Django 4.2 on 2023-12-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_emailverifications_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('agent', 'Agent'), ('manager', 'Manager')], default='agent', max_length=20),
        ),
    ]