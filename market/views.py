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


def index(request):
    return render(request, "market/user/index.html")


def groups(request):
    return render(request, "market/community/groups.html")
