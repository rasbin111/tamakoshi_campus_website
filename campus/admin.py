from django.contrib import admin

from .models import CampusInfo, CampusChiefInfo, StaffInfo, Facility, Testimonial, Programme
from .models import Gallery, Image, Report
from .models import Notice

class CampusInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


class CampusChiefInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    
admin.site.register(CampusInfo, CampusInfoAdmin)
admin.site.register(CampusChiefInfo, CampusChiefInfoAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register([Facility, Testimonial, Report, Notice, Programme, StaffInfo])
