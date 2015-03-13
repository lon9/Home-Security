# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20150311_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intruders',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.TextField(verbose_name='Intruder name', max_length=255)),
                ('timeStamp', models.DateField(verbose_name='Intrusion time', auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Intruder',
        ),
    ]
