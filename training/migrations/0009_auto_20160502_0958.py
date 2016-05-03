# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_auto_20160502_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
