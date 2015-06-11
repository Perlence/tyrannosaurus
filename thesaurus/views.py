from collections import OrderedDict

from django.db.models import Q
from django.shortcuts import render

from .models import Descriptor


def query(request):
    q = request.GET.get('q')
    depth = get_param(request.GET, 'depth', default=1, type=int)
    if not q:
        return render(request, 'index.jinja.html')

    descriptors = (Descriptor.objects
                   .filter(Q(name__icontains=q) | Q(description__icontains=q))
                   .prefetch_related('synonyms',
                                     'parents', 'children',
                                     'higher_level_descriptors', 'lower_level_descriptors',
                                     'part_of', 'consists_of',
                                     'associated_with',
                                     'related_technologically'))
    descriptor_dicts = []
    for descriptor in descriptors:
        descriptor_dicts.append({
            'name': descriptor.name,
            'description': descriptor.description,
            'relations': [
                ('Synonyms', descriptor.synonyms.all()),
                ('Parents', list(get_related(descriptor, 'parents', depth=depth))),
                ('Children', list(get_related(descriptor, 'children', depth=depth))),
                ('Higher level', list(get_related(descriptor, 'higher_level_descriptors', depth=depth))),
                ('Lower level', list(get_related(descriptor, 'lower_level_descriptors', depth=depth))),
                ('Part of', list(get_related(descriptor, 'part_of', depth=depth))),
                ('Consists of', list(get_related(descriptor, 'consists_of', depth=depth))),
                ('Associated with', descriptor.associated_with.all()),
                ('Techno-related', descriptor.related_technologically.all()),
            ]
        })
    return render(request, 'index.jinja.html', {'descriptors': descriptor_dicts})


def get_param(multidict, key, default=None, type=None):
    """Return the default value if the requested data doesn't exist.

    If `type` is provided and is a callable it should convert the value,
    return it or raise a :exc:`ValueError` if that is not possible.  In
    this case the function will return the default as if the value was
    not found.
    """
    try:
        rv = multidict[key]
        if type is not None:
            rv = type(rv)
    except (KeyError, ValueError):
        rv = default
    return rv


def get_related(instance, fieldname, depth=1):
    if depth == 0:
        return
    children = getattr(instance, fieldname)
    for child in children.all():
        yield child
    for child in children.all():
        for grandchild in get_related(child, fieldname, depth=depth - 1):
            yield grandchild
