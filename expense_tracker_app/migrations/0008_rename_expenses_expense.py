# Generated by Django 4.0.4 on 2022-06-09 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker_app', '0007_remove_useramount_count_expenses_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expenses',
            new_name='Expense',
        ),
    ]
