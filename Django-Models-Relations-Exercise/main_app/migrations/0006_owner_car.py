# Generated by Django 5.0.4 on 2025-01-17 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_drivinglicence_drivinglicense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='registration', to='main_app.owner')),
            ],
        ),
    ]
