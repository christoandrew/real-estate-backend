from django.conf.urls import url
from rest_framework import routers

import property.views as estate_property

router = routers.DefaultRouter()
router.register(r'property', estate_property.PropertyViewSet)

urlpatterns = router.urls