from django.contrib import admin
from django.urls import path
from dos.views import dos
from sej.views import sej
from mk.views import mk
from prof.views import prof


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dos/', dos),
    path('sej/', sej),
    path('mk/', mk),
    path('prof/', prof),
]