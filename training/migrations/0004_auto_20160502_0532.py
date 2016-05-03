# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_auto_20160427_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(to='training.Category', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(verbose_name='user photo', null=True, upload_to=''),
        ),
    ]
