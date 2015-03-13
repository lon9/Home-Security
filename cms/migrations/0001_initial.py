# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('timeStamp', models.DateField(auto_now=True, verbose_name='Intrusion time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
