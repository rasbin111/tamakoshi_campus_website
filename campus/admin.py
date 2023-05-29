from django.contrib import admin

from .models import CampusInfo


class CampusInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


admin.site.register(CampusInfo, CampusInfoAdmin)
