# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'complaint_documents', blank=True)),
                ('audio', models.FileField(null=True, upload_to=b'complaint_documents', blank=True)),
                ('video', models.URLField(null=True, blank=True)),
                ('slug', models.SlugField(null=True, editable=False, blank=True)),
                ('ipv4', models.GenericIPAddressField(default=None, null=True, protocol=b'IPv4', blank=True)),
                ('date_create', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(blank=True, to='company.Category', null=True)),
                ('company', models.ForeignKey(blank=True, to='company.Company', null=True)),
                ('subcategory', models.ForeignKey(blank=True, to='company.SubCategory', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraComplaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete_name', models.CharField(max_length=140)),
                ('email', models.EmailField(unique=True, max_length=140)),
                ('cellphone', models.CharField(max_length=140)),
                ('place', models.CharField(max_length=140)),
                ('product_or_service', models.CharField(max_length=140)),
                ('other_solution', models.CharField(max_length=140)),
                ('actions_radio', models.CharField(max_length=140)),
                ('complaint', models.ForeignKey(to='complaint.Complaint')),
            ],
        ),
    ]
