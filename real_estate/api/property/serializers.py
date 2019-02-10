from rest_framework import serializers

from real_estate.api.common.serializers import CountrySerializer, TagSerializer, CitySerializer, AmenitySerializer
from real_estate.cms.models import Property


class PropertySerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()
    type = serializers.CharField(source="type.name")
    country = CountrySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    city = CitySerializer(read_only= True)
    amenities = AmenitySerializer(read_only=True, many=True)

    class Meta:
        model = Property
        fields = ('id', 'name', 'type', 'country', 'city',
                  'photo', 'tags', 'amenities')
