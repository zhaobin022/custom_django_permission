# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_group',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_group',
            field=models.ForeignKey(blank=True, to='polls.UserGroup', null=True),
        ),
    ]
