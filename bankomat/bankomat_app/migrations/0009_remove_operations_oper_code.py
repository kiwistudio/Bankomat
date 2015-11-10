# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0008_operations_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operations',
            name='oper_code',
        ),
    ]
