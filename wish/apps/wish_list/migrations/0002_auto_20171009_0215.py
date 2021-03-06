# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='wisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_wishes', to='wish_list.User'),
        ),
        migrations.AlterField(
            model_name='wish',
            name='wishers',
            field=models.ManyToManyField(related_name='wishes', to='wish_list.User'),
        ),
    ]
