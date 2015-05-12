# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=b'category_logos', blank=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(upload_to=b'subcategory_logos', blank=True),
        ),
    ]
