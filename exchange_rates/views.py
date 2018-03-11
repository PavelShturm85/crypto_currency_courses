from django.utils import timezone
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Currency
from .forms import CurrencyFilterForm
# Create your views here.


def exchange_rates_list(request):
    currency_list = Currency.objects.filter(last_updated__lte=timezone.now()).order_by('-last_updated')
    form = CurrencyFilterForm()
    if form.is_valid():
        if form.cleaned_data["min_date"]:
            currency_list = currency_list.filter(last_updated__gte=form.cleaned_data["min_date"])
        if form.cleaned_data["max_date"]:
            currency_list = currency_list.filter(last_updated__lte=form.cleaned_data["max_date"])
    
    paginator = Paginator(currency_list, 15)
    page = request.GET.get('page')
    try:
        currency = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        currency = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        currency = paginator.page(paginator.num_pages)

    return render_to_response('exchange_rates/exchange_rates_list.html', {'currency':currency, 'form':form})
    

"""
def exchange_rates_list(request):
    currency = Currency.objects.filter(last_updated__lte=timezone.now()).order_by('-last_updated')
    return render(request, 'exchange_rates/exchange_rates_list.html', {'currency':currency})
"""