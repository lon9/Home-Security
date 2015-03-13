# -*-coding: utf-8 -*-
from django.forms import ModelForm
from cms.models import Intruder

class IntruderForm(ModelForm):
    class Meta:
        model = Intruder
        fields = ('name',)