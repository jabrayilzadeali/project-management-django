# Generated by Django 4.0.4 on 2022-06-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker_app', '0004_useramount_expenses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='count',
        ),
        migrations.AddField(
            model_name='useramount',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='useramount',
            name='expenses',
            field=models.ManyToManyField(related_name='expenses', to='expense_tracker_app.expenses'),
        ),
        migrations.AlterField(
            model_name='useramount',
            name='pay',
            field=models.DecimalField(decimal_places=True, default=0, max_digits=10),
        ),
    ]
