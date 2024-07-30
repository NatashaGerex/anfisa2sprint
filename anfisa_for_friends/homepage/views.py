from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream, Category


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description', 'price'
        ).filter(Q(is_on_main=True)
                 & Q(is_published=True)
                 & Q(category__is_published=True)
        )
    # categories = Category.objects.values(
    #     'id', 'output_order', 'title'
    # ).order_by('output_order', 'title')
    context = {'ice_cream_list': ice_cream_list, }
    # context = {'categories': categories}
    return render(request, template, context)
