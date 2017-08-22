from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^analysis/', include('analysis.urls')),
]
