# Generated by Django 2.1 on 2019-04-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t', '0010_auto_20190419_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]