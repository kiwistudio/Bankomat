# -*- coding: utf-8 -*-
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    cardowner = Cardowner.objects.get(pk=pk)
    if request.method == "POST":
        if request.POST.get('balance') is not None:   
            now_time = datetime.datetime.now() + datetime.timedelta(hours=2)
            data = {'oper_table':cardowner,
            		'description': u'Просмотр баланса',
            		'data_time': str(now_time)[:-7]
            	}
            oper = Operations(**data)
            oper.save()	            
            return HttpResponseRedirect(u'balance/')
        if request.POST.get('get_cash') is not None:
            return HttpResponseRedirect(u'get_cash/')
        if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Operation/operations.html')


def balance(request, pk):
    cardowner = Cardowner.objects.get(pk=pk)
    oper = Operations.objects.filter(oper_table=pk)
    now_date = datetime.date.today()
    

    # paginate operations
    paginator = Paginator(oper, 3)
    page = request.GET.get('page')
    try:
        oper = paginator.page(page)
        cardowner = Cardowner.objects.get(pk=pk)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        oper = paginator.page(1)
    except EmptyPage:
    # last page of results.
        cardowner = Cardowner.objects.get(pk=pk)
        oper = paginator.page(paginator.num_pages)

    context = {'cardowner':cardowner,
            'empty':'0',
            'now_date':now_date,
            'oper':oper}

    if request.method == "POST":
        if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Operation/balance.html', context)


def get_cash(request, pk):
    cardowner = Cardowner.objects.get(pk=pk)
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
                cardowner.balance = balance
                cardowner.save()
                now_time = datetime.datetime.now() + datetime.timedelta(hours=2)
                data = {'oper_table':cardowner,
            		    'description': u'Снятие наличных:%s' % get_cash,
            		    'data_time': str(now_time)[:-7]
            	    }
                oper = Operations(**data)
                oper.save()	
                oper = Operations.objects.filter(oper_table=pk)
                context = {'cardowner':cardowner,
                           'now_time':now_time,
                           'empty':'0',
                           'oper':oper,
                           'get_cash':get_cash}     
        if not errors:
            return render(request, 'Operation/report.html', context)
        else:
            messages.success(request, u'%s' % errors['error'])
            return render(request, 'Validation/error.html', {})
    return render(request, 'Operation/get_cash.html', {})


def report(request, pk):
    # cardowner = Cardowner.objects.get(pk=pk)
    # oper = Operations.objects.get(oper_table=pk)
    if request.method == "POST":
        if request.POST.get('exit') is not None:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Operation/report.html', context)
