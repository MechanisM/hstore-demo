from django.db import models

from django.db import models
from django_hstore import hstore

class Product(models.Model):
    name = models.CharField(max_length=250)
    data = hstore.DictionaryField(db_index=True)
    objects = hstore.Manager()

    def __unicode__(self):
        return self.name
