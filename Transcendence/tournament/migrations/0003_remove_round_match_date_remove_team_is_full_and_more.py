# Generated by Django 4.2.11 on 2024-04-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_alter_team_players_alter_team_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='match_date',
        ),
        migrations.RemoveField(
            model_name='team',
            name='is_full',
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
