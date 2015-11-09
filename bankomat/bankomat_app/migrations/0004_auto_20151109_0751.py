# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0003_cardowner_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardowner',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='\u0411\u0430\u043b\u0430\u043d\u0441'),
        ),
    ]
