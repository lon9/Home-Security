# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150311_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intruder',
            name='timeStamp',
            field=models.DateTimeField(verbose_name='Intrusion time', auto_now=True),
            preserve_default=True,
        ),
    ]
