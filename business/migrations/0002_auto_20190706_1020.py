# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-06 07:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_user.Neighbourhood'),
        ),
    ]
