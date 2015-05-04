# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0004_complaint_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='company',
            field=models.ForeignKey(to='company.Company', null=True),
        ),
    ]
