# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


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
                ('slug', models.SlugField(null=True, editable=False, blank=True)),
                ('ipv4', models.GenericIPAddressField(default=None, null=True, protocol=b'IPv4', blank=True)),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_approved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='company.Category', null=True)),
                ('company', models.ForeignKey(blank=True, to='company.Company', null=True)),
                ('subcategory', models.ForeignKey(blank=True, to='company.SubCategory', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete_name', models.CharField(max_length=140, null=True, blank=True)),
                ('email', models.EmailField(max_length=140, null=True, blank=True)),
                ('cellphone', models.CharField(max_length=140, null=True, blank=True)),
                ('complaint', models.ForeignKey(to='complaint.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=140, null=True, blank=True)),
                ('product_or_service', models.CharField(max_length=140, null=True, blank=True)),
                ('other_solution', models.CharField(max_length=140, null=True, blank=True)),
                ('complaint', models.ForeignKey(to='complaint.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='ComplaintRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actions_radio', models.CharField(blank=True, max_length=140, null=True, choices=[(0, b'Que me proponga una solucion'), (1, b'La devolucion de mi Dinero'), (2, b'Que entregue mi producto'), (3, b'Otra solucion')])),
                ('complaint', models.ForeignKey(to='complaint.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='ItemFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'complaint_documents', blank=True)),
                ('audio', models.FileField(null=True, upload_to=b'complaint_documents', blank=True)),
                ('complaint', models.ForeignKey(blank=True, to='complaint.Complaint', null=True)),
            ],
        ),
    ]
