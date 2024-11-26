from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def tv(request):
    return HttpResponse('all brands are available')
