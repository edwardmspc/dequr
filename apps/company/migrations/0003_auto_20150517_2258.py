# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_auto_20150517_2258'),
        ('company', '0002_auto_20150510_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.ForeignKey(blank=True, to='category.Category', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='subcategory',
            field=models.ForeignKey(blank=True, to='category.SubCategory', null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
