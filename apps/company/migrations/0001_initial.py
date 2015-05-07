# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('image', models.ImageField(upload_to=b'company_logos', blank=True)),
                ('category', models.ForeignKey(blank=True, to='company.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('slug', models.SlugField(editable=False)),
                ('category', models.ForeignKey(blank=True, to='company.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('company', models.ForeignKey(blank=True, to='company.Company', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='subcategory',
            field=models.ForeignKey(blank=True, to='company.SubCategory', null=True),
        ),
    ]
