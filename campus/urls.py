from django.urls import path
from .views import home, about_us, programmes, admission_details, notices, ContactView, publications, gallery, \
            message_success_view, notice_detail

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('programmes/', programmes, name='programmes'),
    path('admission-details/', admission_details, name='admission-details'),
    path('notices/', notices, name='notices'),
    path('notice/<slug:slug>/', notice_detail, name='notice-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/message-success/', message_success_view, name='message-success'),
    path('publications/', publications, name='publications'),
    path('gallery/', gallery, name='gallery'),

]
