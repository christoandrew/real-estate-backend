from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('real_estate.site.urls', namespace='real_estate.site')),
    url(r'^cms/', include('real_estate.cms.urls', namespace='real_estate.cms')),
    url(r'^api/', include('real_estate.api.urls', namespace='real_estate.api')),
    url(r'^admin/', admin.site.urls),
]
