# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0005_auto_20151109_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oper_code', models.CharField(max_length=256, verbose_name='\u043d\u043e\u043c\u0435\u0440 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('oper_table', models.ForeignKey(verbose_name='\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446 \u043a\u0430\u0440\u0442\u044b', to='bankomat_app.Cardowner')),
            ],
            options={
                'verbose_name': '\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043a\u0430\u0440\u0442\u044b',
                'verbose_name_plural': '\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u043a\u0430\u0440\u0442',
            },
        ),
    ]
