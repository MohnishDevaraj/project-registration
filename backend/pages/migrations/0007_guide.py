# Generated by Django 4.0.4 on 2022-06-11 14:58

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_delete_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField(default=1)),
                ('serial_no', models.IntegerField()),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('domain_1', models.CharField(max_length=200)),
                ('domain_2', models.CharField(blank=True, max_length=200)),
                ('domain_3', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('experience', models.IntegerField()),
                ('myImage', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('vacancy', models.IntegerField(default=7)),
            ],
        ),
    ]
