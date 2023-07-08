from django.shortcuts import render

from campus.models import Notice


def notices(request):
    notices = Notice.valid_objects.all()
    return render(request, 'notices.html', {'notices': notices})

def notice_detail(request, slug):
    notice = Notice.valid_objects.get(slug=slug)
    return render(request, 'notice_detail.html', {'notice': notice})
