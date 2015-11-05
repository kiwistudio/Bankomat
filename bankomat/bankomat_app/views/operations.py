# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# from ..models import Cardowner


# Views for Students
def operations(request):
    # students = Student.objects.all()
	
    return render(request, 'Operation/operations.html', {})


def balance(request):

	return render(request, 'Operation/balance.html', {})


def get_cash(request):

	return render(request, 'Operation/get_cash.html', {})


def report(request):

	return render(request, 'Operation/report.html', {})
