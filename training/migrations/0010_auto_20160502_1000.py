# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0009_auto_20160502_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
