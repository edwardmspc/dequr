# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_complaint_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='category',
            field=models.ForeignKey(to='category.Category', null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='subcategory',
            field=models.ForeignKey(blank=True, to='category.SubCategory', null=True),
        ),
    ]
