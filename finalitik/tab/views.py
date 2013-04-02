from django.shortcuts import render, get_object_or_404
from tab.models import Tab


def index(request):
    zadnje_tabele = Tab.objects.order_by('datum')[:4]
    context = {'zadnje_tabele': zadnje_tabele}
    return render(request, 'tab/index.html', context)


def detail(request, id):
    tab = get_object_or_404(Tab, pk=id)
    return render(request, 'tab/detail.html', {'Tab': tab})
