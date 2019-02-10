from django.conf.urls import url

from real_estate.cms import views

urlpatterns = [
    url(r'^', view=views.index)
]