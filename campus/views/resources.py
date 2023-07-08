import os
from django.shortcuts import render
from campus.models import Gallery, Report


def publications(request):
    reports = Report.objects.all()
    for report in reports:
        report.file_name = os.path.basename(report.report_file.name)
    return render(request, 'publications.html', {'publications': reports})


def gallery(request):
    galleries = Gallery.objects.all()

    for gallery in galleries:
        gallery.images_list.clear()
        for image in gallery.images.all():
            gallery.images_list.append(image.image.url)
    return render(request, 'gallery.html', {'galleries': galleries})