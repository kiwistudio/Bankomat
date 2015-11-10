# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0009_remove_operations_oper_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='operations',
            name='oper_code',
            field=models.IntegerField(default=0, verbose_name='\u043d\u043e\u043c\u0435\u0440 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438'),
        ),
    ]
