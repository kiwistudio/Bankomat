# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardowner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=256, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('middle_name', models.CharField(default=b'', max_length=256, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True)),
                ('cardnumber', models.CharField(max_length=256, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b')),
                ('pin_code', models.CharField(max_length=256, verbose_name='\u041f\u0438\u043d-\u043a\u043e\u0434')),
                ('card_block', models.BooleanField(default=False, max_length=256)),
            ],
            options={
                'ordering': ('last_name',),
                'verbose_name': '\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446 \u043a\u0430\u0440\u0442\u044b',
                'verbose_name_plural': '\u0412\u043b\u0430\u0434\u0435\u043b\u044c\u0446\u044b \u043a\u0430\u0440\u0442\u044b',
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
