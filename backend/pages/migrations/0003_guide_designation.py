# Generated by Django 4.0.4 on 2022-06-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
