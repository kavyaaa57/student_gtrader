# Generated by Django 4.2.1 on 2023-05-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdftool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
