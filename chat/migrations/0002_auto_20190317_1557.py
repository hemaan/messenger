# Generated by Django 2.1.5 on 2019-03-17 15:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='porfile',
            new_name='Profile',
        ),
    ]
