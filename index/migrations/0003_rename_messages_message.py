# Generated by Django 4.2.4 on 2023-08-10 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_messages_ourvision'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='messages',
            new_name='message',
        ),
    ]