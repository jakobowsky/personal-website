# Generated by Django 2.2 on 2019-04-23 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_githubpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githubpost',
            old_name='uel',
            new_name='url',
        ),
    ]
