# Generated by Django 3.1.1 on 2020-12-30 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achieve', '0006_auto_20201230_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achieve.kin'),
        ),
    ]