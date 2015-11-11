# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0011_auto_20151110_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operations',
            name='oper_code',
        ),
    ]
