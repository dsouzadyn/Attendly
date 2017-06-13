# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0002_auto_20170314_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('semester', models.IntegerField()),
                ('subject_name', models.CharField(max_length=128)),
                ('abbr', models.CharField(max_length=30)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendence.Branch')),
            ],
        ),
    ]