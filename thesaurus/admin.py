from django.contrib import admin

from .models import Descriptor


class DescriptorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')

admin.site.register(Descriptor, DescriptorAdmin)
