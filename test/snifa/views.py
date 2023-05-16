from django.shortcuts import render
from snifa.models import Result
from . import web_scraper
from django.http import JsonResponse

def index(request):
    result = Result.objects.all()
    return render(request, "snifa/index.html", {'result':result})

def scrape_data(request):
    result = web_scraper.scrape_data()
    return JsonResponse(result, safe=False)