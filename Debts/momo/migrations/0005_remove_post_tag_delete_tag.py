# Generated by Django 5.1.5 on 2025-02-01 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('momo', '0004_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
