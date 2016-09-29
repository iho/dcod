# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Country, Region


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Region, RegionAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'value')
    list_filter = ('region',)
    search_fields = ('name',)
admin.site.register(Country, CountryAdmin)
