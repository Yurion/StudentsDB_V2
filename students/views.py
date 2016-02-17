from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

def students_list(request):
    return HttpResponse('<h1>Hello World</h1>')

def students_list2(request, sid):
    try:
        sid = int(sid)
    except ValueError:
        raise Http404
    else:
        return HttpResponse('<h1>Hello World</h1>')

def students_list3(request):
    template = loader.get_template('demo.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def students_list4(request):
    return render(request, 'demo.html', {})