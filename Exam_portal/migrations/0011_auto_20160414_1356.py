# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_portal', '0010_auto_20160414_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]