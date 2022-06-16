from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from KDBES.models import  Rinfo,Bevent,Zlocation,Zremarks,Areg
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from kenlist import settings


def home_page(request):
    return render(request, 'homepage.html')
def home_log(request):
 if request.method == 'POST':
        if Rinfo.objects.filter(runame=request.POST['rruname'], rpass=request.POST['rrpass']).exists():
            rinfo_ = Rinfo.objects.get(runame=request.POST['rruname'], rpass=request.POST['rrpass'])
            return redirect(f'{rinfo_.id}/next')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'homepage.html', context)

def admin_log(request):
 if request.method == 'POST':
        if Areg.objects.filter(ausername=request.POST['aausername'], apassword=request.POST['aapassword']).exists():
            areg_ = Areg.objects.get(ausername=request.POST['aausername'], apassword=request.POST['aapassword'])
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'admin.html')

def Login(request):
    next = request.GET.get('next', '/adminbook/')
    if request.method == "POST":
        if Areg.objects.filter(ausername=request.POST['aausername'], apassword=request.POST['aapassword']).exists():
            areg_ = Areg.objects.get(ausername=request.POST['aausername'], apassword=request.POST['aapassword'])
            return HttpResponseRedirect(next)
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, "admin.html", {'redirect_to': next})



def new_list(request):
    srinfo = Rinfo.objects.create(rlname=request.POST['lastname'],rfname=request.POST['firstname'],rmname=request.POST['middlename'],raddress=request.POST['rraddress'],rage=request.POST['rrage'],rcnumber=request.POST['rccnumber'],runame=request.POST['rruname'],rpass=request.POST['rrpass'])
    return redirect(f'{srinfo.id}/next')


def view_list(request, rinfo_id):
    #locations = Location.objects.all()
    rinfo_ = Rinfo.objects.get(id=rinfo_id)
    return render(request, 'eventinfo.html',{'rinfo': rinfo_})

def add_item(request, rinfo_id):
    rinfo_ = Rinfo.objects.get(id=rinfo_id)
    Bevent.objects.create(blocation=request.POST['bblocation'],bmainevent=request.POST['bbmainevent'],bdate=request.POST['bbdate'],bbstime=request.POST['bbbstime'],bbetime=request.POST['bbbetime'],bhours=request.POST['bbhours'],bpeople=request.POST['bbpeople'],brates=request.POST['bbrates'],rinfo=rinfo_)
    return redirect(f'/{rinfo_.id}/next')


def register(request):
    rinfos = Rinfo.objects.all()
    return render(request, 'register.html', {'rinfos':rinfos})

def eventview(request, rinfo_id):
    #locations = Location.objects.all()
    rinfo_ = Rinfo.objects.get(id=rinfo_id)
    return render(request, 'eventview.html', {'rinfo':rinfo_})


#for Admin Views
def adminbook(request):
    rinfos = Rinfo.objects.all()
    return render(request, 'adminbooklist.html', {'rinfos':rinfos})

def eventstatus(request, rinfo_id):
    #locations = Location.objects.all()
    rinfo_ = Rinfo.objects.get(id= rinfo_id)
    return render(request, 'eventstatus.html', {'rinfo':rinfo_})

def statusupdate(request, rinfo_id):
    rinfo = Bevent.objects.get(id=rinfo_id)
    rinfo.bstatus= request.POST['bbstatus']
    rinfo.save()
    return redirect(f'/{rinfo.id}/eventstatus')


def aaccount(request):
    ainfos = Ainfo.objects.all()
    return render(request, 'account.html', {'ainfos':ainfos})

def zad(request):
    if 'next' in request.POST:
        return redirect(request.POST.get('next'))
    else:
        return render(request, 'admin.html')



#This is for adding Location in eventinfo
def add_location(request, id):
   if request.method == "POST":
    zlocation = Zlocation.objects.get(id=id)
    zlocations.objects.create(llocation=request.POST['lllocation'],laddress=request.POST['lladdress'])
    zlocations.save()
    
   return redirect('/location')



def view_location(request):
    zlocations = Zlocation.objects.all()
    return render(request, 'LocationReg.html', {'zlocation':zlocations})


def edit(request, id):
    rinfos = Rinfo.objects.get(id=id)
    context = {'rinfos': rinfos}
    return render(request, 'edit.html', context)

def update(request, id):
    rinfo = Rinfo.objects.get(id=id)
    rinfo.rlname = request.POST['rrlname']
    rinfo.rage = request.POST['rrage']
    rinfo.rcnumber = request.POST['rrcnumber']
    rinfo.rruname = request.POST['rruname']
    rinfo.rrpass = request.POST['rrpass']
    rinfo.save()
    return redirect('/')
def delete(request, id):
    rinfo = Rinfo.objects.get(id=id)
    rinfo.delete()
    return redirect('/')






def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def Schedule(request):
    return render(request, 'Schedule.html')

# Create your views here.
#def index(request):
    #if request.method == 'POST':
        #member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        #member.save()
        #return redirect('/')
    #else:
        #return render(request, 'index.html')
'''

#from django.http import HttpResponse    
from django.shortcuts import redirect, render
from KDBES.models import  Rinfo,Bevent,Zlocation,Zremarks,Areg

def home_page(request): 
     rinfos = Rinfo.objects.all()
     return render(request, 'regpage.html',{'rinfos' : rinfos})

def add_item(request):     
   newrinfo_ = Rinfo.objects.create(rlname=request.POST['lastname'],rfname=request.POST['firstname'],rmname=request.POST['middlename'],
    raddress=request.POST['rraddress'],rage=request.POST['rrage'],rcnumber=request.POST['rccnumber'],runame=request.POST['rruname'],
    rpass=request.POST['rrpass'])
   return redirect(f'/{newrinfo_.id}/') 

def view_list(request, rinfo_id):    
   rinfo_ = Rinfo.objects.get(id=rinfo_id)
   return render(request, 'eventpage.html', {'rinfo': rinfo_})

  
def add_info(request, rinfo_id):    
   rinfo_ = Rinfo.objects.get(id=rinfo_id)    
   Bevent.objects.create(blocation=request.POST['bblocation'],bcategory=request.POST['bbcategory'],bdate=request.POST['bbdate'],
    bbstime=request.POST['bbbstime'],bbetime=request.POST['bbbetime'],bpeople=request.POST['bbpeople'],bhours=request.POST['bbhours'],rinfo=rinfo_)
   return redirect(f'/{rinfo_.id}/')    
  

def register(request):
    rinfos = Rinfo.objects.all()
    return render(request, 'register.html', {'rinfos':rinfos})

















'''










   

  











