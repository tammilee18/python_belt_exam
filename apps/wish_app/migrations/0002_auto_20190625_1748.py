# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-25 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='granted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='granted_wish', to='wish_app.User'),
        ),
    ]
