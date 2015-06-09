# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(null=True, blank=True)),
                ('associated_with', models.ManyToManyField(related_name='associated_with_rel_+', to='thesaurus.Descriptor', blank=True)),
                ('higher_level_descriptors', models.ManyToManyField(related_name='lower_level_descriptors', to='thesaurus.Descriptor', blank=True)),
                ('parents', models.ManyToManyField(related_name='children', to='thesaurus.Descriptor', blank=True)),
                ('part_of', models.ManyToManyField(related_name='consists_of', to='thesaurus.Descriptor', blank=True)),
                ('related_technologically', models.ManyToManyField(related_name='related_technologically_rel_+', to='thesaurus.Descriptor', blank=True)),
                ('synonym', models.ManyToManyField(related_name='synonym_rel_+', to='thesaurus.Descriptor', blank=True)),
            ],
        ),
    ]
