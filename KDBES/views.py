from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html', {'idNew': request.POST.get('brgyid'), 'FNameNew': request.POST.get('FresName'), 
		'MNameNew': request.POST.get('MresName'), 'LNameNew': request.POST.get('LresName'), 
		'AddressNew': request.POST.get('resAddress'), 'AgeNew': request.POST.get('resAge'), 'BdayNew': request.POST.get('resBday'),
		'ContactNew': request.POST.get('resContact')})