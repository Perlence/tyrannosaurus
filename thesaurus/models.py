from django.db import models


class Descriptor(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    synonym = models.ManyToManyField('self', blank=True)
    parents = models.ManyToManyField('self', related_name='children', symmetrical=False, blank=True)
    higher_level_descriptors = models.ManyToManyField('self', related_name='lower_level_descriptors', symmetrical=False, blank=True)
    part_of = models.ManyToManyField('self', related_name='consists_of', symmetrical=False, blank=True)
    associated_with = models.ManyToManyField('self', blank=True)
    related_technologically = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return unicode(self.name)
