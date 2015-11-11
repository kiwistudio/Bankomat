# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from ..models import Cardowner


# Home page
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

	
tries = 4
# pin validation page
def pin_code(request, pk):
    global tries
    cardowner = Cardowner.objects.get(pk=pk)
    if request.method == "POST":
        if request.POST.get('ok') is not None:
            pin_code = request.POST.get('pin_code', '').strip()
            if pin_code != cardowner.pin_code:
                tries -= 1
                if tries == 0:
                    tries = 4
                    cardowner.card_block = True
                    cardowner.save()
                    messages.success(request, u'Карта заблокирована!')
                    return HttpResponseRedirect(reverse('error2'))
                return render(request, 'Validation/pin_code.html', {'tries':tries})
            else:
                return HttpResponseRedirect(u'operations/')
        if request.POST.get('back') is not None:
            return render(request, 'Validation/cardnumber.html', {})
	
    return render(request, 'Validation/pin_code.html', {'tries':tries})

# Error page
def error(request):
    
    return render(request, 'Validation/error.html', {})

# Error2 page
def error2(request):
    if request.method == "POST":
        if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Validation/error2.html', {})