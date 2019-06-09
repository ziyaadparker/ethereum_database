from django.shortcuts import render
from django.http import HttpResponse
from front_app.models import EthereumKeys
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    ethkeys = EthereumKeys.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(ethkeys, 10)
    try:
        ethkeys = paginator.page(page)
    except PageNotAnInteger:
        ethkeys = paginator.page(1)
    except EmptyPage:
        ethkeys = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'ethkeys': ethkeys})
