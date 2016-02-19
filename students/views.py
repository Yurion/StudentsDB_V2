from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader


# View for Students

def students_list(request):
    return render(request, 'students/students_list.html', {})

def students_add(requst):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(requst, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(requst, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def group_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(requst):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(requst, sid):
    return HttpResponse('<h1>Edit Group %s</h1>' % sid)

def groups_delete(requst, sid):
    return HttpResponse('<h1>Delete Group %s</h1>' % sid)



















# def students_list2(request, sid):
#     try:
#         sid = int(sid)
#     except ValueError:
#         raise Http404
#     else:
#         return HttpResponse('<h1>Hello World</h1>')
#
#
# def students_list3(request):
#     template = loader.get_template('demo.html')
#     context = RequestContext(request, {})
#     return HttpResponse(template.render(context))
#
#
# def students_list4(request):
#     return render(request, 'demo.html', {})
