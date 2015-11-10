# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0010_operations_oper_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operations',
            name='data',
        ),
        migrations.AddField(
            model_name='operations',
            name='data_time',
            field=models.CharField(max_length=256, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438'),
        ),
    ]
