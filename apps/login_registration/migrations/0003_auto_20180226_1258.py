# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 17:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0002_auto_20180226_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last',
        ),
    ]
