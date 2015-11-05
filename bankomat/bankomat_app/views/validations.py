# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# from ..models import Cardowner


# Views for Students
def cardnumber(request):
    # students = Student.objects.all()
	
    return render(request, 'Validation/cardnamber.html', {})


def pin_code(request):
    # students = Student.objects.all()
	
    return render(request, 'Validation/pin_code.html', {})


def error(request):

	return render(request, 'Validation/error.html', {})