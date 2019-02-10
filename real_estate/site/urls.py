from django.conf.urls import url

from real_estate.site import views

urlpatterns = [
    url(r'^', view=views.index)
]