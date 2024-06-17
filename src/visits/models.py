from django.db import models

class pageVisit(models.Model):
    path  = models.TextField(null=True,blank=True)
    timestamp = models.DateField(auto_now_add=True)
