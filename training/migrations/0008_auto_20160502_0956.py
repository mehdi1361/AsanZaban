# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_auto_20160502_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='level',
            field=models.IntegerField(choices=[(1, 'beginer'), (2, 'very easy'), (3, 'easy'), (4, 'hard'), (5, 'very hard')], default=1),
        ),
    ]
