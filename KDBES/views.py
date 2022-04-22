from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html', {'NameNew': request.POST.get('resName'), 'FNameNew': request.POST.get('FresName'), 'LNameNew': request.POST.get('LresName'), 'MAddressNew': request.POST.get('MresAddress')})