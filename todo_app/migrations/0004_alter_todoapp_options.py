# Generated by Django 4.0.4 on 2022-05-31 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_rename_user_todoapp_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoapp',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
