# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student


def students_list(request):
    students = Student.objects.all().order_by('last_name')

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('number', 'last_name', 'first_name', 'ticket'):
        if order_by == 'number':
            students = students.order_by('id')
        else:
            students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    return render(request, 'students/students_list.html', {"students": students, "request": request})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
