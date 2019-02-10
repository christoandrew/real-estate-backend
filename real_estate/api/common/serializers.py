from rest_framework import serializers

from real_estate.cms.models import Country, Tag, District, AmenityType


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityType
        fields = ('id', 'name')
