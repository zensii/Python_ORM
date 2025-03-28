# Generated by Django 5.0.4 on 2025-03-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actor_movies', to='main_app.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Other', 'Other')], default='Other', max_length=6),
        ),
    ]
