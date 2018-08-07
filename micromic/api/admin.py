from django.contrib import admin
from .models import DailyLogList, MaintenanceList

class DailyLogListAdmin(admin.ModelAdmin):
    list_display = ("date_created", "name", "upload")
    list_filter = ("date_created",)
    search_fields = ("name", "date_created")
    class Meta:
            model = DailyLogList

class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ("date_created", "comment",)
    list_filter = ("date_created",)
    search_fields = ("comment", "date_created")
    class Meta:
            model = DailyLogList

admin.site.register(DailyLogList, DailyLogListAdmin)
admin.site.register(MaintenanceList, MaintenanceLogAdmin)
