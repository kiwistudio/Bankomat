# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Cardowner

# class for add a parametres to register models
class CardownerAdmin(admin.ModelAdmin): # inheritance from django.contrib.admin
	list_display = ('last_name', 'first_name', 'cardnumber', 'pin_code') # display a table in admin
	list_display_links = ['last_name', 'first_name']
	list_per_page = 10
	search_fields = ['last_name', 'first_name', 'cardnumber', 'pin_code'] # searching in tables
	ordering = ('last_name',) # sorted by last_name in admin site


admin.site.register(Cardowner, CardownerAdmin) # add a parametres to register

