# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 17:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0048_rack_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rackreservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
