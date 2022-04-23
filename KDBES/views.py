from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html', {'idNew': request.POST.get('brgyid'), 'FNameNew': request.POST.get('FresName'), 'LNameNew': request.POST.get('LresName'), 'MAddressNew': request.POST.get('MresAddress')})