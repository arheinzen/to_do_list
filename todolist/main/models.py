from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=30, null=True)
    date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=100, blank=True)
    status = models.BooleanField()
    
    def __str__(self):
        return self.name 