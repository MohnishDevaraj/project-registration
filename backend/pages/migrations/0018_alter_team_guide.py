# Generated by Django 4.0.4 on 2022-06-21 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_alter_team_guide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pages.guide'),
        ),
    ]
