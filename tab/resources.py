from tastypie.resources import ModelResource
from tab.models import Tab


class TabResource(ModelResource):
    class Meta:
        queryset = Tab.objects.all()
        resource_name = 'tab'