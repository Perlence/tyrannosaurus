from django.db.models import Q
from django.shortcuts import render

from .models import Descriptor


def query(request):
    q = request.GET.get('q')
    if not q:
        return render(request, 'index.html')

    descriptors = (Descriptor.objects
                   .filter(Q(name__icontains=q) | Q(description__icontains=q))
                   .prefetch_related('synonyms',
                                     'parents', 'children',
                                     'higher_level_descriptors', 'lower_level_descriptors',
                                     'part_of', 'consists_of',
                                     'associated_with',
                                     'related_technologically'))
    return render(request, 'index.html', {'descriptors': descriptors})
