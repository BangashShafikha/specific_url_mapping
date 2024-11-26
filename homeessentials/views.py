from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kitchenware(request):
    return HttpResponse('all kitchen items are available')
