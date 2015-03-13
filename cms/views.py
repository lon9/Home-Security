from django.shortcuts import render, render_to_response, redirect,\
    get_object_or_404
from django.http.response import HttpResponse
from django.template.context import RequestContext
from cms.models import Intruder
from cms.forms import IntruderForm

# Create your views here.
def intruder_list(request):
    #return HttpResponse(u'侵入者情報')
    intruders = Intruder.objects.all().order_by('id')
    return render_to_response('cms/intruder_list.html',
                              {'intruders': intruders},
                              context_instance=RequestContext(request))
    
def intruder_edit(request, intruder_id=None):
    #return HttpResponse(u'侵入者の編集')
    
    if intruder_id:
        intruder = get_object_or_404(Intruder, pk=intruder_id)
    else:
        intruder = Intruder()
    
    if request.method=='POST':
        form = IntruderForm(request.POST, instance=intruder)
        if form.is_valid():
            intruder = form.save(commit=False)
            intruder.save()
            return redirect('cms:intruder_list')
    else:
        form = IntruderForm(instance=intruder)
        
    return render_to_response('cms/intruder_edit.html',
                              dict(form=form, intruder_id=intruder.id),
                              context_instance=RequestContext(request))
    
def intruder_del(request, intruder_id):
    #return HttpResponse(u'侵入者の削除')
    intruder = get_object_or_404(Intruder, pk=intruder_id)
    intruder.delete()
    return redirect('cms:intruder_list')
    