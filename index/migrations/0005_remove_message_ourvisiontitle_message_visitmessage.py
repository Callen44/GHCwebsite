# Generated by Django 4.2.4 on 2023-08-13 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_message_ourvisiontitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='ourvisiontitle',
        ),
        migrations.AddField(
            model_name='message',
            name='visitmessage',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
