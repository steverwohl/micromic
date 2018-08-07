from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView, MaintenanceDetailsView, MaintenanceView
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'api'

urlpatterns = {
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dailyloglists/', CreateView.as_view(), name="create"),
    path('dailyloglists/<int:pk>/', DetailsView.as_view(), name="details"),
    path('maintenancelog/', MaintenanceView.as_view(), name="create"),
    path('maintenancelog/<int:pk>/', MaintenanceDetailsView.as_view(), name="details"),
    path('users/', UserView.as_view(), name="users"),
    path('users/<int:pk>/', UserDetailsView.as_view(), name="user_details"),
    path('get-token/', obtain_auth_token),

    #re_path(r'^dailyloglists/(?P<pk>[0-9]+)/$',
    #    DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
