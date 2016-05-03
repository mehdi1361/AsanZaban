# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='category name')),
                ('parent', models.ForeignKey(to='training.Category')),
            ],
            options={
                'db_table': 'categories',
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Package name')),
            ],
            options={
                'db_table': 'packages',
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='provider name')),
                ('icon', models.ImageField(null=True, verbose_name='provider icon', upload_to='')),
            ],
            options={
                'db_table': 'providers',
                'verbose_name': 'Provider',
                'verbose_name_plural': 'Providers',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='user name')),
                ('password', models.CharField(max_length=12, verbose_name='user password')),
                ('mobile', models.CharField(max_length=20, verbose_name='user mobile')),
                ('email', models.CharField(max_length=50, verbose_name='user email')),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female')], verbose_name='gender', default=1)),
                ('birth_date', models.DateTimeField(null=True, verbose_name='user birthdate')),
                ('photo', models.ImageField(null=True, verbose_name='user birthdate', upload_to='')),
            ],
            options={
                'db_table': 'users',
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
