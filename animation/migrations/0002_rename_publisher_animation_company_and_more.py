# Generated by Django 4.0.5 on 2022-06-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animation',
            old_name='publisher',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='animation',
            old_name='summary',
            new_name='story',
        ),
        migrations.RemoveField(
            model_name='animation',
            name='genre',
        ),
        migrations.AddField(
            model_name='animation',
            name='genre',
            field=models.ManyToManyField(related_name='animations', to='animation.genre'),
        ),
    ]