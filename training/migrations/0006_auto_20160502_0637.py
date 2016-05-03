# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20160502_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created_time',
        ),
        migrations.RemoveField(
            model_name='userpackage',
            name='last_view_time',
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')], default=1),
        ),
        migrations.AlterField(
            model_name='package',
            name='category',
            field=models.ForeignKey(to='training.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='package',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(),
        ),
    ]
