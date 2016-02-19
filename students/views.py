# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader


# View for Students

def students_list(request):
    # return render(request, 'students/students_list.html', {})
    students = (
        {
            'id': 1,
            'first_name': u'Віталій',
            'last_name': u'Подоба',
            'ticket': 235,
            'image': 'img/podoba3.jpg'
        },

        {
            'id': 2,
            'first_name': u'Корост',
            'last_name': u'Андрій',
            'ticket': 2123,
            'image': 'img/me.jpeg'
        },

        {
            'id': 3,
            'first_name': u'Притула',
            'last_name': u'Тарас',
            'ticket': 5332,
            'image': 'img/piv.png'
        },
    )
    return render(request, 'students/students_list.html', {'students': students})


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
