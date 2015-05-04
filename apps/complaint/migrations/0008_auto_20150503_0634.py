# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0007_auto_20150503_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='ipv4',
            field=models.CharField(max_length=140, null=True, blank=True),
        ),
    ]
