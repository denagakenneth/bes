from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	# if request.method == 'POST':
	# 	return HttpResponse (request.POST['attribute'])
	return render(request, 'mainpage.html', {'NewName': request.POST.get('attribute'),})

def MainPage(request):
	# if request.method == 'POST':
	# 	return HttpResponse (request.POST['attribute'])
	return render(request, 'mainpage.html', {'NewAge': request.POST.get('attribute'),})