from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("mainsite.urls")),
    path('admin/', include("adminsite.urls")),
    path('reserveadmin/', admin.site.urls)
]
