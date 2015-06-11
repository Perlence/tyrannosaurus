from django.contrib import admin
from django import forms

from .models import Descriptor

all_descriptors = Descriptor.objects.all()


class DescriptorForm(forms.ModelForm):
    children = forms.ModelMultipleChoiceField(all_descriptors, required=False)
    lower_level_descriptors = forms.ModelMultipleChoiceField(all_descriptors, required=False)
    consists_of = forms.ModelMultipleChoiceField(all_descriptors, required=False)

    class Meta:
        model = Descriptor
        fields = ('name',
                  'description',
                  'synonyms',
                  'parents', 'children',
                  'higher_level_descriptors', 'lower_level_descriptors',
                  'part_of', 'consists_of',
                  'associated_with', 'related_technologically')

    def __init__(self, *args, **kwargs):
        super(DescriptorForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        self.prepare_reverse_relations(instance, 'children')
        self.prepare_reverse_relations(instance, 'lower_level_descriptors')
        self.prepare_reverse_relations(instance, 'consists_of')

    def prepare_reverse_relations(self, instance, fieldname):
        """Provide initial values for symmetrical relations and wrap the
        fields in RelatedFieldWidgetWrapper."""
        field = self.fields[fieldname]
        parents = self.fields['parents']

        if instance is not None:
            related_manager = getattr(instance, fieldname)
            field.initial = related_manager.all()

        widget = field.widget
        rel = getattr(Descriptor, fieldname).related
        admin_site = parents.widget.admin_site
        wrapped = admin.widgets.RelatedFieldWidgetWrapper(widget, rel, admin_site)
        field.widget = wrapped
        field.help_text = parents.help_text

    def save(self, commit=True):
        descriptor = super(DescriptorForm, self).save(commit=False)

        if commit:
            descriptor.save()

        reverse_relations = {'children', 'lower_level_descriptors', 'consists_of'}
        if reverse_relations.intersection(self.changed_data):
            if not descriptor.pk:
                descriptor.save()
            descriptor.children = self.cleaned_data['children']
            descriptor.lower_level_descriptors = self.cleaned_data['lower_level_descriptors']
            descriptor.consists_of = self.cleaned_data['consists_of']
            self.save_m2m()

        return descriptor


class DescriptorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    form = DescriptorForm

admin.site.register(Descriptor, DescriptorAdmin)
