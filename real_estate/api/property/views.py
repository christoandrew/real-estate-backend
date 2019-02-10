from rest_framework import viewsets

from real_estate.api.property.serializers import PropertySerializer
from real_estate.cms.models import Property


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
