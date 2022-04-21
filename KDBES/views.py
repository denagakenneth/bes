from django.shortcuts import render
from django.http import  HttpResponse

def MainPage(request):
	return HttpResponse('<html><title>Chrono Intelligence - World News</title></html>')
# Create your views here.
