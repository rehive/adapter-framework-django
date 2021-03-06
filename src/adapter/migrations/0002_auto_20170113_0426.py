# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-13 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adapter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(db_index=True, max_length=100, unique=True)),
                ('token', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='adminaccount',
            name='service_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adapter.ServiceAccount'),
        ),
    ]
