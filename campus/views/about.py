from django.shortcuts import render
from campus.models import CampusInfo, CampusChiefInfo, StaffInfo, Programme

def about_us(request):
    campus = CampusInfo.objects.first()
    campus_chief = CampusChiefInfo.objects.first()
    staffs = StaffInfo.objects.all()
    return render(request, 'about.html', {'campus_chief': campus_chief, 'staffs': staffs, 'campus': campus})


def programmes(request):
    programmes = Programme.objects.all()
    return render(request, 'programmes.html', {'programmes': programmes})


def admission_details(request):
    return render(request, 'admission.html')

