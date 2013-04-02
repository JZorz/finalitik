from datetime import timedelta, datetime
from django.db import models
from django.utils import timezone


class Tab(models.Model):
    konto = models.CharField(max_length=200)
    znesek = models.IntegerField(default=0)
    datum = models.DateTimeField('datum')

    def nedavno(self):
        return self.datum >= timezone.now() - timedelta(days=1)
    nedavno.admin_order_field = 'datum'
    nedavno.boolean = True
    nedavno.short_description = 'Nedavno dodano?'