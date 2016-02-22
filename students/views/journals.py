# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


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
