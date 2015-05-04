# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('complete_name', models.CharField(max_length=140, null=True, blank=True)),
                ('email', models.EmailField(max_length=140, unique=True, null=True, blank=True)),
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
        migrations.RemoveField(
            model_name='extracomplaint',
            name='complaint',
        ),
        migrations.DeleteModel(
            name='ExtraComplaint',
        ),
    ]
