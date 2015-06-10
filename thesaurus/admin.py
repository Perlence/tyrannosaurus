from django.contrib import admin
from django import forms

from .models import Descriptor

all_descriptors = Descriptor.objects.all()


class DescriptorForm(forms.ModelForm):
    children = forms.ModelMultipleChoiceField(all_descriptors, required=False)
    lower_level_descriptors = forms.ModelMultipleChoiceField(all_descriptors, required=False)
    consists_of = forms.ModelMultipleChoiceField(all_descriptors, required=False)

    def __init__(self, *args, **kwargs):
        super(DescriptorForm, self).__init__(*args, **kwargs)
        # Provide initial values for related m2m fields.
        instance = kwargs.get('instance')
        if instance is None:
            return
        self._set_initial(instance, 'children')
        self._set_initial(instance, 'lower_level_descriptors')
        self._set_initial(instance, 'consists_of')

    def _set_initial(self, instance, fieldname):
        related_manager = getattr(instance, fieldname)
        self.fields[fieldname].initial = [item.pk for item in related_manager.all()]

    class Meta:
        model = Descriptor
        fields = ('name',
                  'description',
                  'synonyms',
                  'parents', 'children',
                  'higher_level_descriptors', 'lower_level_descriptors',
                  'part_of', 'consists_of',
                  'associated_with', 'related_technologically')


class DescriptorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    form = DescriptorForm

    def save_model(self, request, obj, form, change):
        self._save_m2m_field(obj, form, 'children')
        self._save_m2m_field(obj, form, 'lower_level_descriptors')
        self._save_m2m_field(obj, form, 'consists_of')
        return super(DescriptorAdmin, self).save_model(request, obj, form, change)

    def _save_m2m_field(self, obj, form, fieldname):
        if fieldname not in form.changed_data:
            return
        field = form.fields[fieldname]
        data = form.data.get(fieldname, [])
        setattr(obj, fieldname, field.to_python(data))

admin.site.register(Descriptor, DescriptorAdmin)
