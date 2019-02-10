# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Property Type"
        verbose_name_plural = "Property Types"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AmenityType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    PAYMENT_OPTIONS = (
        ("LEASE", "LEASE"),
        ("MONTHLY", "MONTHLY"),
        ("QUATERLY", "QUATERLY"),
        ("ANNUAL", "ANNUAL"),
        ("OTHER", "OTHER")
    )
    id = models.IntegerField
    name = models.CharField(max_length=255, choices=PAYMENT_OPTIONS)

    def __str__(self):
        return self.name


class Photo(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()
    type = models.CharField(max_length=10)
    image = models.ImageField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        pass


class Property(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(District, on_delete=models.CASCADE)
    amenities = models.ManyToManyField(AmenityType)
    photo = models.ImageField(upload_to='property/%Y/%m/%d')
    tags = models.ManyToManyField(Tag)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    review = models.TextField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return "{} -  {} - {}".format(self.user.username, self.property.name, self.review)

