# Generated by Django 4.0.4 on 2022-06-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='count',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='price',
            field=models.DecimalField(decimal_places=True, max_digits=10),
        ),
    ]
