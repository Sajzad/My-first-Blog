# Generated by Django 2.1.5 on 2019-02-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='visited',
            field=models.BooleanField(default=True),
        ),
    ]
