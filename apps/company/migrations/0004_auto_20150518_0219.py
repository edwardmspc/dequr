# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20150517_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 5, 18, 2, 18, 32, 127661, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='facebook',
            field=models.CharField(default=datetime.datetime(2015, 5, 18, 2, 18, 39, 93763, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default=datetime.datetime(2015, 5, 18, 2, 18, 43, 652103, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='twitter',
            field=models.CharField(default=datetime.datetime(2015, 5, 18, 2, 18, 50, 90821, tzinfo=utc), max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='web_url',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(unique=True, max_length=140),
        ),
    ]
