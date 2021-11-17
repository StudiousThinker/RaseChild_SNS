from django.db import models
from django.db.models.fields import CharField,TextField,IntegerField

# Create your models here.

CHOICE = (('danger','high'),('success','normal'),('primary','low'))

class BoadModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    contributor = models.CharField(max_length=20)
    good = models.IntegerField(null=True, blank=True, default=1)
    priority = models.CharField(max_length=10,choices=CHOICE)
    follow = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
    
