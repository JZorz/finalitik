from django.contrib import admin
from tab.models import Tab


class TabAdmin(admin.ModelAdmin):
    list_display = ('konto', 'znesek', 'datum', 'nedavno')
    list_filter = ['datum']
    search_fields = ['konto']
    date_hierarchy = 'datum'


admin.site.register(Tab, TabAdmin)
