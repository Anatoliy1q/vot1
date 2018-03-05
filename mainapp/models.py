from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateField()
    
    