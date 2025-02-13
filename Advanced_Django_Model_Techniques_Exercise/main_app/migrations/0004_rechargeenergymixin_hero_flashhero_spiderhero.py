# Generated by Django 5.0.4 on 2025-01-26 08:19

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_product_discountedproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='RechargeEnergyMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('rechargeenergymixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.rechargeenergymixin')),
                ('name', models.CharField(max_length=100)),
                ('hero_title', models.CharField(max_length=100)),
                ('energy', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Energy cannot drop below 1')])),
            ],
            bases=('main_app.rechargeenergymixin',),
        ),
        migrations.CreateModel(
            name='FlashHero',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.hero',),
        ),
        migrations.CreateModel(
            name='SpiderHero',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.hero',),
        ),
    ]
