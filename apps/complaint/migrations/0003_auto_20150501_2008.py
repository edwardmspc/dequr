# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_auto_20150501_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='date_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='complaintcontact',
            name='email',
            field=models.EmailField(max_length=140, null=True, blank=True),
        ),
    ]
