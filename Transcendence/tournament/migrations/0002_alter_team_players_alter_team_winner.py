# Generated by Django 4.2.11 on 2024-04-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0001_initial'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='tournaments', to='pong.usercustom'),
        ),
        migrations.AlterField(
            model_name='team',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_teams', to='pong.usercustom'),
        ),
    ]