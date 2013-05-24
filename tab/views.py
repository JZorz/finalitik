from django.shortcuts import render, get_object_or_404
from tab.models import Tab


def index(request):
    zadnje_tabele = Tab.objects.raw('SELECT * FROM tab_Tab GROUP BY groupname')
    context = {'zadnje_tabele': zadnje_tabele}
    return render(request, 'tab/index.html', context)


def detail(request, id):
    tab = get_object_or_404(Tab, pk=id)
    gn = tab.groupname
    tb = Tab.objects.raw('SELECT * FROM tab_Tab WHERE groupname = %s', [gn])
    context = {'group': tb}
    return render(request, 'tab/detail.html', context)
