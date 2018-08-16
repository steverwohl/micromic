from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from api.models import DailyLogList, MaintenanceList


def homepage(request, slug='index'):
    queryset = DailyLogList.objects.latest('date_created')
    context = {
        'slug': slug,
        'object' : queryset,
    }
    return render(request, "index.html", context)


def dailylogs(request, slug='dailylogs'):
    query = request.GET.get('datefilter')
    queryset = DailyLogList.objects.all()
    if (query):
        dates = query.split(' - ')
        queryset = queryset.filter(date_created__lte=dates[1], date_created__gte=dates[0])
    else:
        queryset = queryset[::-1]
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {
        'slug': slug,
        "object_list" : queryset,
        'title': 'List',
    }
    return render(request, "dailylogs.html", context)


def dailylog_detail(request, dailylog_id):
    dailylog = get_object_or_404(DailyLogList, pk= dailylog_id)
    context = {
        'title': dailylog.name,
        'instance': dailylog,
    }
    return render(request, "dailylog_detial.html", context)


def maintenancelogs(request, slug="maintenancelogs"):
    queryset = MaintenanceList.objects.all()
    context = {
        'slug' : slug,
        'object_list' : queryset,
        'title': 'List',
    }
    return render(request, "maintenancelogs.html", context)


def maintenancelog_detail(request, maintenancelog_id):
    maintenancelog = get_object_or_404(MaintenanceList, pk=maintenancelog_id)
    context = {
        'title': maintenancelog.date_created,
        'instance': maintenancelog,
    }
    return render(request, "maintenancelog_detial.html", context)
