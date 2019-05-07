# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waffle_utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaffleFlagDashboardCourseLoadCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_count', models.IntegerField(default=250)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Waffle flag Lms Dashboard Course Count',
                'verbose_name_plural': 'Waffle flag Lms Dashboard Course Count',
            },
        ),
    ]
