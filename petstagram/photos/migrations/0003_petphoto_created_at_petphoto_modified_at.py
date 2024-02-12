# Generated by Django 5.0.2 on 2024-02-10 20:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_rename_petphotos_petphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petphoto',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]