from django.shortcuts import render

from campus.models import Testimonial, Facility

def home(request):
    testimonials = Testimonial.objects.all()
    facilities = Facility.objects.all()
    return render(request, 'home.html', {'testimonials': testimonials, 'facilities': facilities})
