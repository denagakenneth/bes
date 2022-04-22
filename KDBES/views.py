from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html', {'NameNew': request.POST.get('studentName'), 'FNameNew': request.POST.get('FstudentName'), 'LNameNew': request.POST.get('LstudentName'), 'MNameNew': request.POST.get('MstudentName')})