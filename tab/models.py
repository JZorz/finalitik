from datetime import timedelta
from django.db import models
from django.utils import timezone


class Tab(models.Model):
    konto = models.CharField(max_length=256)
    groupname = models.CharField(max_length=256)
    znesek = models.FloatField(default=0.0)
    datum = models.DateTimeField('datum')

    def nedavno(self):
        return self.datum >= timezone.now() - timedelta(days=1)
    nedavno.admin_order_field = 'datum'
    nedavno.boolean = True
    nedavno.short_description = 'Nedavno dodano?'

    def __unicode__(self):
        return "%s %s %s" % (self.konto, self.groupname, self.znesek)
