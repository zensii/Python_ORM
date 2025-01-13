# Generated by Django 5.0.4 on 2025-01-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='class_name',
            field=models.CharField(choices=[('Mage', 'Mage'), ('Warrior', 'Warrior'), ('Assassin', 'Assassin'), ('Scout', 'Scout')], max_length=20),
        ),
    ]
