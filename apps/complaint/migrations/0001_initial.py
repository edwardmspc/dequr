# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(editable=False)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=255, blank=True)),
                ('date_create', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('category', models.ForeignKey(to='complaint.Category', blank=True)),
            ],
        ),
    ]
