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


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def group_list(request):
    groups = (
        {
            'id': 1,
            'group_name': u'МтМ-21',
            'leader': {'id': 1, 'name': u'Ячменев Олег'},
        },

        {
            'id': 2,
            'group_name': u'МтМ-22',
            'leader': {'id': 2, 'name': u'	Віталій Подоба'},
        },

        {
            'id': 3,
            'group_name': u'МтМ-23',
            'leader': {'id': 3, 'name': u'Іванов Андрій'},
        },
    )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)

# Views for Visiting

def visiting_list(request):
    students = (
        {
            'id': 1,
            'name': u'Ячменев Олег'
        },
        {
            'id': 2,
            'name': u'Віталій Подоба'
        },
        {
            'id': 3,
            'name': u'Іванов Андрій'
        },
    )
    return render(request, 'students/visiting_list.html', {'students': students})







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
