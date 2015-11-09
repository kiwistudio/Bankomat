# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from ..models import Cardowner, Operations

# if there is an alpha in a string       
def ifalpha(text):
    lit, num = '', ''
    for ch in text:
        if ch.isalpha(): lit += ch
        else: num += ch
    if lit: return True
    else: return False
  

# Views for Students
def operations(request, pk):
    if request.method == "POST":
    	if request.POST.get('balance') is not None:
            now_time = datetime.datetime.now()
            oper = Operations.objects.get(oper_table=pk)
            oper.description  += u'%s\nПросмотр баланса\n' % now_time
            oper.oper_code += 1
            oper.save()
            return HttpResponseRedirect(u'balance/')
    	if request.POST.get('get_cash') is not None:
            return HttpResponseRedirect(u'get_cash/')
        if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Operation/operations.html')


def balance(request, pk):
    cardowner = Cardowner.objects.get(pk=pk)
    oper = Operations.objects.get(oper_table=pk)
    now_date = datetime.date.today()
    context = {'cardowner':cardowner,
            'now_date':now_date,
            'empty':'0',
            'oper':oper}
    if request.method == "POST":
        if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Operation/balance.html', context)


def get_cash(request, pk):
    cardowner = Cardowner.objects.get(pk=pk)
    oper = Operations.objects.get(oper_table=pk)
    if request.method == "POST":
    	errors  = {}
    	if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
        if request.POST.get('ok') is not None:
            get_cash = request.POST.get('get_cash', '').strip()
            if get_cash == '' or get_cash == '0' or ifalpha(get_cash) == True :
                errors['error'] = u'Введите сумму для снятия средств'
                messages.success(request, u'%s' % errors['error'])
                return render(request, 'Validation/error.html', {})
            balance = cardowner.balance - int(get_cash)
            if balance < 0:
                errors['error'] = u'На Вашем счету недостаточно средств для снятия суммы'
            else:
                now_time = datetime.datetime.now()
                cardowner.balance = balance
                cardowner.save()
                oper.description  += u'%s\nСнято %s\n' % (now_time, get_cash)
                oper.oper_code += 1
                oper.save()
                now_time = datetime.datetime.now()
                context = {'cardowner':cardowner,
                           'now_time':now_time,
                           'empty':'0',
                           'oper':oper,
                           'get_cash':get_cash}     
        if not errors:
            return HttpResponseRedirect(reverse('report'), context)
        else:
            messages.success(request, u'%s' % errors['error'])
            return render(request, 'Validation/error.html', {})
    return render(request, 'Operation/get_cash.html', {})


def report(request, pk):
    if request.method == "POST":
        if request.POST.get('back') is not None:
            return render(request, 'Operation/operations.html', {})
        if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Operation/report.html', context)
