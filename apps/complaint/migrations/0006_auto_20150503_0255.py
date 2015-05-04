# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_auto_20150503_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='company',
            field=models.ForeignKey(default=1, to='company.Company'),
            preserve_default=False,
        ),
    ]
