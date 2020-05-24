from django.http import HttpResponse
from django.shortcuts import render

from .models import *

app_name = "market"


def home(request):
    content = {'all_products': Product.objects.all()}
    return render(request, "market/mall/home.html", content)


def sort(request):
    return render(request, "market/mall/sort.html")


def error(request):
    return render(request, "market/util/error.html")


def profile(request):
    return render(request, "market/user/profile.html")


def article(request):
    return render(request, "market/user/article.html")


def sell(request):
    return render(request, "market/user/sell.html")


def community(request):
    return render(request, "market/user/community.html")


def buy(request):
    return render(request, "market/user/buy.html")


def groups(request):
    return render(request, "market/community/groups.html")
