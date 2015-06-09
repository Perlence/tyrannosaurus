# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descriptor',
            name='synonym',
        ),
        migrations.AddField(
            model_name='descriptor',
            name='synonyms',
            field=models.ManyToManyField(related_name='synonyms_rel_+', to='thesaurus.Descriptor', blank=True),
        ),
    ]
