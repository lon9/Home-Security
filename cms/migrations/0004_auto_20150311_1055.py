# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20150311_1054'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Intruders',
            new_name='Intruder',
        ),
    ]
