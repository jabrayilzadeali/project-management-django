# Generated by Django 4.0.4 on 2022-05-31 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_rename_task_todoapp_rename_title_todoapp_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoapp',
            old_name='user',
            new_name='author',
        ),
    ]
