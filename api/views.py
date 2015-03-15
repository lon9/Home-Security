from django.shortcuts import render
from collections import OrderedDict
from django.http import HttpResponse
from cms.models import Intruder
from cms.forms import IntruderForm
import json

# Create your views here.
def render_json_response(request, data, status=None):
    '''GETの結果'''
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.REQUEST.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8'
                                , status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8'
                                , status=status)
    return response

def intruder_list(request):
    '''侵入者情報を返す'''
    intruders = [];
    for intruder in Intruder.objects.all().order_by('id'):
        
        intruder_dict = OrderedDict([
                                     ('id', intruder.id),
                                     ('name', intruder.name),
                                     ('timeStamp', intruder.timeStamp.isoformat())
                                     ])
        intruders.append(intruder_dict)
        
    data = OrderedDict([('intruders', intruders)])
    return render_json_response(request, data)

def arduino_post(request):
    intruder = Intruder()
    
    form = IntruderForm(request.POST, instance=intruder)
    intruder = form.save(commit=False)
    intruder.save()
    data = "OK"
    
    return render_json_response(request, data)
    
    