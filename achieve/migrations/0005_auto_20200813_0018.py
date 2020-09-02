# Generated by Django 3.0.5 on 2020-08-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achieve', '0004_auto_20200812_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]