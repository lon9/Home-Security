from django.db import models
import datetime

# Create your models here.
class Intruder(models.Model):
    '''侵入者情報'''
    name = models.TextField('Intruder name', max_length=255, default='Intruder')
    timeStamp = models.DateTimeField('Intrusion time', auto_now=True)
    
    def __str__(self):
        return self.name