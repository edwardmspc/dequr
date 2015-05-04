# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0006_auto_20150503_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.ForeignKey(to='company.Category', null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='company',
            field=models.ForeignKey(blank=True, to='company.Company', null=True),
        ),
    ]
