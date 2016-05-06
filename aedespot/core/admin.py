from django.contrib import admin

from .models import Report


class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'type')
    list_filter = ('type',)


admin.site.register(Report, ReportModelAdmin)
