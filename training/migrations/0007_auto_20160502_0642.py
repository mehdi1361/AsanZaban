# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_auto_20160502_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_enable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='package',
            name='is_enable',
            field=models.BooleanField(default=False),
        ),
    ]
