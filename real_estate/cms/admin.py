# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import models, TextInput

from .models import Property, Type, Country, District, AmenityType, Tag, PaymentType


class PropertyAdminForm(models.ModelForm):
    amenities = models.ModelMultipleChoiceField(queryset=AmenityType.objects.all(),
                                                widget=FilteredSelectMultiple(("amenities"), False),
                                                label=("Select Amenities."))
    tags = models.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                           label="Select tags",
                                           widget=FilteredSelectMultiple("tags", False))

    class Meta:
        model = Property
        fields = "__all__"

    class Media:
        def __init__(self):
            pass

        css = {
            'all': "/media/css/widgets.css"
        }

        js = "/admin/jsi18n/"

    def clean(self):
        cleaned_data = super(PropertyAdminForm, self).clean()

        return cleaned_data


class PropertyAdmin(admin.ModelAdmin):
    model = Property
    list_display = ('id', 'name', 'type', 'city', 'country')

    form = PropertyAdminForm


class TagAdminForm(models.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'})
        }


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    form = TagAdminForm


admin.site.register(Property, PropertyAdmin)
admin.site.register(Type)
admin.site.register(Country)
admin.site.register(District)
admin.site.register(AmenityType)
admin.site.register(Tag, TagAdmin)
admin.site.register(PaymentType)
