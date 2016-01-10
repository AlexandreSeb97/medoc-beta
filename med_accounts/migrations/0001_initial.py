# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('country', models.CharField(max_length=255)),
                ('specialite', models.CharField(max_length=255)),
                ('owner_first_name', models.CharField(max_length=120)),
                ('owner_last_name', models.CharField(max_length=120)),
                ('is_member', models.BooleanField(default=False, verbose_name='Is Paid Member')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
