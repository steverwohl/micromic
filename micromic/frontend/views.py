from django.shortcuts import render, get_object_or_404

from api.models import DailyLogList, MaintenanceList


def homepage(request, slug='index'):
    context = {
        'slug': slug,
    }
    return render(request, "index.html", context)


def dailylogs(request, slug='dailylogs'):
    queryset = DailyLogList.objects.all()
    context = {
        'slug': slug,
        "object_list" : queryset,
        "title": "List",
    }
    return render(request, "dailylogs.html", context)


def dailylog_detail(request, dailylog_id):
    dailylog = get_object_or_404(DailyLogList, pk= dailylog_id)
    context = {
        "title": dailylog.name,
        "instance": dailylog,
    }
    return render(request, "dailylog_detial.html", context)


def maintenancelogs(request):
    queryset = MaintenanceList.objects.all()
    context = {
        "object_list" : queryset,
        "title": "List",
    }
    return render(request, "maintenancelogs.html", context)


def maintenancelog_detail(request, maintenancelog_id):
    maintenancelog = get_object_or_404(MaintenanceList, pk=maintenancelog_id)
    context = {
        "title": maintenancelog.date_created,
        "instance": maintenancelog,
    }
    return render(request, "maintenancelog_detial.html", context)
