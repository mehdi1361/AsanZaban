# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20160427_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='card title')),
                ('description', models.TextField(verbose_name='card description')),
                ('additonal_info', models.CharField(max_length=50, verbose_name='card additonal_info')),
                ('hard_ship', models.CharField(max_length=50, verbose_name='card hard_ship')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
                'db_table': 'cards',
            },
        ),
        migrations.CreateModel(
            name='CardLog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('log_time', models.DateTimeField(auto_now_add=True)),
                ('answer_state', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Card_Log',
                'verbose_name_plural': 'Card_Logs',
                'db_table': 'card_logs',
            },
        ),
        migrations.CreateModel(
            name='CardMedia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('media_type', models.IntegerField(choices=[(1, 'text'), (2, 'image'), (3, 'sound'), (4, 'video')])),
                ('content', models.CharField(max_length=250)),
                ('card', models.ForeignKey(to='training.Card')),
            ],
            options={
                'verbose_name': 'Information_Card',
                'verbose_name_plural': 'Information_Cards',
                'db_table': 'card_informations',
            },
        ),
        migrations.CreateModel(
            name='CardState',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('last_view_time', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField()),
                ('card', models.ForeignKey(to='training.Card')),
                ('user', models.ForeignKey(to='training.User')),
            ],
            options={
                'verbose_name': 'Card_State',
                'verbose_name_plural': 'Card_States',
                'db_table': 'card_states',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.IntegerField(choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')], default=1)),
                ('is_moderated', models.BooleanField(default=False)),
                ('package', models.ForeignKey(to='training.Package')),
                ('user', models.ForeignKey(to='training.User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='lesson name')),
                ('order', models.IntegerField(choices=[(1, 'order 1'), (2, 'order 2'), (3, 'order 3'), (4, 'order 4'), (5, 'order 5')], default=1)),
                ('package', models.ForeignKey(to='training.Package')),
            ],
            options={
                'verbose_name': 'Lesson',
                'verbose_name_plural': 'Lessons',
                'db_table': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='UserPackage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_view_time', models.DateTimeField(null=True)),
                ('finish_time', models.DateTimeField(null=True)),
                ('is_archive', models.BooleanField(default=False)),
                ('package', models.ForeignKey(to='training.Package')),
                ('user', models.ForeignKey(to='training.User')),
            ],
            options={
                'verbose_name': 'UserPackage',
                'verbose_name_plural': 'userpackages',
                'db_table': 'user_packages',
            },
        ),
        migrations.AddField(
            model_name='cardlog',
            name='card_state',
            field=models.ForeignKey(to='training.CardState'),
        ),
    ]
