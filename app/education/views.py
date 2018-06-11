from django.http import HttpResponse
from django.shortcuts import render

from education.models import School


def school_list(requset):
    schools = School.objects.all()
    context = {
        'schools':schools
    }
    return render(requset, 'education/school_list.html', context)

def school_detail(request, school_id):
    schools = School.objects.get(id=school_id)
    context = {
        'schools': schools,
    }
    return render(request, 'education/deatil.html', context)