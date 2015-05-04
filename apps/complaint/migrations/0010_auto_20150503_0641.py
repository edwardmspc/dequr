# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0009_auto_20150503_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(null=True, editable=False, blank=True),
        ),
    ]
