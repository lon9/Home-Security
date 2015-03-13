# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20150311_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intruder',
            name='name',
            field=models.TextField(max_length=255, default='Intruder', verbose_name='Intruder name'),
            preserve_default=True,
        ),
    ]
