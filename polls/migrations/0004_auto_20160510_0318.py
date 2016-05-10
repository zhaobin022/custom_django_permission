# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='\u5730\u5740'),
        ),
    ]
