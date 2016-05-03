# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='category',
            field=models.ForeignKey(verbose_name='Category', null=True, to='training.Category'),
        ),
        migrations.AddField(
            model_name='package',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='package',
            name='discount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='level',
            field=models.IntegerField(default=1, choices=[(1, 'beginer'), (2, 'very easy'), (3, 'easy'), (4, 'hard'), (5, 'very easy')]),
        ),
        migrations.AddField(
            model_name='package',
            name='photo',
            field=models.ImageField(upload_to='', null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='provider',
            field=models.ForeignKey(verbose_name='Provider', null=True, to='training.Provider'),
        ),
    ]
