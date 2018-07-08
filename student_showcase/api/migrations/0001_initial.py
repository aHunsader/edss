# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_description', models.TextField()),
                ('rep_1_name', models.CharField(max_length=30)),
                ('rep_1_email', models.EmailField(max_length=30)),
                ('rep_1_phone', models.CharField(max_length=12)),
                ('rep_2_name', models.CharField(max_length=30)),
                ('rep_2_email', models.EmailField(max_length=30)),
                ('rep_2_phone', models.CharField(max_length=12)),
                ('special_needs', models.TextField()),
            ],
        ),
    ]