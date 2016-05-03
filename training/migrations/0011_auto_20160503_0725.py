# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0010_auto_20160502_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='lesson',
            field=models.ForeignKey(to='training.Lesson', default=1),
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(verbose_name='Package description', blank=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='discount',
            field=models.IntegerField(verbose_name='Package name', default=0),
        ),
        migrations.AlterField(
            model_name='package',
            name='is_enable',
            field=models.BooleanField(verbose_name='Package enable', default=False),
        ),
        migrations.AlterField(
            model_name='package',
            name='level',
            field=models.IntegerField(choices=[(1, 'beginer'), (2, 'very easy'), (3, 'easy'), (4, 'hard'), (5, 'very hard')], verbose_name='Package level', default=1),
        ),
        migrations.AlterField(
            model_name='package',
            name='photo',
            field=models.ImageField(verbose_name='Package photo', blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(verbose_name='Package price', default=0),
        ),
    ]
