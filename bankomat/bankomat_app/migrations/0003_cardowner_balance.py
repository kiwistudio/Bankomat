# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0002_auto_20151105_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardowner',
            name='balance',
            field=models.FloatField(default=0, verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441'),
        ),
    ]
