# Generated by Django 3.0.5 on 2020-08-12 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achieve', '0003_auto_20200812_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='text',
            new_name='title',
        ),
    ]
