# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160509_0434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_name', models.CharField(max_length=64, verbose_name='\u670d\u52a1\u5668\u540d')),
                ('ip', models.IPAddressField(verbose_name='\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
    ]
