# Generated by Django 4.1.4 on 2024-01-28 12:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_categories_parent_name_alter_parts_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.location'),
        ),
        migrations.AlterField(
            model_name='parts',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='parts',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]