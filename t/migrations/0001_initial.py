# Generated by Django 2.1 on 2019-04-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('drug', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('pincode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='stores',
            field=models.ManyToManyField(to='t.Store'),
        ),
        migrations.AddField(
            model_name='disease',
            name='medicines',
            field=models.ManyToManyField(to='t.Medicine'),
        ),
        migrations.AddField(
            model_name='disease',
            name='symptoms',
            field=models.ManyToManyField(to='t.Symptom'),
        ),
    ]
