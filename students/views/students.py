# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student


def students_list(request):
    # return render(request, 'students/students_list.html', {})
    # students = (
    #     {
    #         'id': 1,
    #         'first_name': u'Віталій',
    #         'last_name': u'Подоба',
    #         'ticket': 235,
    #         'image': 'img/podoba3.jpg'
    #     },
    #
    #     {
    #         'id': 2,
    #         'first_name': u'Корост',
    #         'last_name': u'Андрій',
    #         'ticket': 2123,
    #         'image': 'img/me.jpeg'
    #     },
    #
    #     {
    #         'id': 3,
    #         'first_name': u'Притула',
    #         'last_name': u'Тарас',
    #         'ticket': 5332,
    #         'image': 'img/piv.png'
    #     },
    # )

    students = Student.objects.all()
    return render(request, 'students/students_list.html', {"students": students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
