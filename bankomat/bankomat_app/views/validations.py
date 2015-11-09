# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages

from ..models import Cardowner


# Views for Students
def cardnumber(request):

    if request.method == "POST":
        if request.POST.get('ok') is not None:
            # errors collection
            errors = {}
            cardnumber = request.POST.get('cardnumber', '').strip()
            if len(cardnumber) != 19:
                errors['cardnumber'] = u"Введите верный номер карты"
            else:
                try:
                    cardowner = Cardowner.objects.get(cardnumber=cardnumber)
                    if cardowner.card_block == True:
                        errors['cardnumber'] = u"Карта заблокирована!"
                except:
                    errors['cardnumber'] = u"Номер карты не существует"
				
            if not errors:
                tries = 4
                return HttpResponseRedirect(u'pin_code/%s/' % str(cardowner.id), {'tries':tries})
            else:
                messages.success(request, u'%s' % errors['cardnumber'])
                return render(request, 'Validation/error.html', {})
    return render(request, 'Validation/cardnumber.html')		
	


def pin_code(request, pk):
    cardowner = Cardowner.objects.get(pk=pk)
    if request.method == "POST":
        if request.POST.get('ok') is not None:
            pin_code = request.POST.get('pin_code', '').strip()
            if pin_code != cardowner.pin_code:
                tries = 4-1
                if tries == 0:
                    cardowner.card_block == True
                    cardowner.save()
                    messages.success(request, u'Карта заблокирована!')
                    return render(request, 'Validation/error.html', {})
                return render(request, 'Validation/pin_code.html', {'tries':tries})
            else:
                return HttpResponseRedirect(u'operations/')
        if request.POST.get('back') is not None:
            return render(request, 'Validation/cardnumber.html', {})
	
    return render(request, 'Validation/pin_code.html', {'tries':4})


def error(request):
    
    return render(request, 'Validation/error.html', {})