# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0004_auto_20151109_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardowner',
            name='balance',
            field=models.FloatField(default=0, verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441'),
        ),
    ]
