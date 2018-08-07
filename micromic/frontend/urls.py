from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import dailylog_detail, dailylogs, maintenancelogs, maintenancelog_detail

app_name = 'frontend'

urlpatterns = {
    path('dailylogs/', dailylogs, name = 'dailylogs'),
    path('dailylogs/<int:dailylog_id>/', dailylog_detail, name='dailylog_detail'),
    path('maintenancelogs/', maintenancelogs, name = 'maintenancelogs'),
    path('maintenancelogs/<int:maintenancelog_id>/', maintenancelog_detail, name='maintenancelog_detail'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
