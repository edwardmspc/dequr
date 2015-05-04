# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0008_auto_20150503_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='ipv4',
            field=models.GenericIPAddressField(default=None, null=True, protocol=b'IPv4', blank=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
