#from django.http import HttpResponse    
from django.shortcuts import redirect, render
from KDBES.models import  Rinfo,Bevent,Zlocation,Zremarks,Areg

def home_page(request): 
     rinfos = Rinfo.objects.all()
     return render(request, 'a.html',{'rinfos' : rinfos})

  
def add_info(request, rinfo_id):    
   rinfo_ = Rinfo.objects.get(id=rinfo_id)    
   Bevent.objects.create(blocation=request.POST['bblocation'],bcategory=request.POST['bbcategory'],bdate=request.POST['bbdate'],rinfo=rinfo_)
   return redirect(f'/{rinfo_.id}/')    
   
def view_list(request, rinfo_id):    
   rinfo_ = Rinfo.objects.get(id=rinfo_id)
   return render(request, 'b.html', {'rinfo': rinfo_})
   
def add_item(request):     
   newrinfo_ = Rinfo.objects.create(rlname=request.POST['lastname'],rfname=request.POST['firstname'],rmname=request.POST['middlename'])
   return redirect(f'/{newrinfo_.id}/') 
  












'''from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from KDBES.models import  Rinfo,Bevent,Zlocation,Zremarks,Areg
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from kenlist import settings


def home_page(request):
    return render(request, 'a.html')
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
    srinfo = Rinfo.objects.create(rlname=request.POST['rrlname'],rfname=request.POST['rrfname'],rmname=request.POST['rrmname'],raddress=request.POST['rraddress'],rage=request.POST['rrage'],rcnumber=request.POST['rccnumber'],runame=request.POST['rruname'],rpass=request.POST['rrpass'])
    return redirect(f'{srinfo.id}/next')


def view_list(request, rinfo_id):
    locations = Location.objects.all()
    rinfo_ = Rinfo.objects.get(id=rinfo_id)
    return render(request, 'abooking.html',{'rinfo': rinfo_,'location':locations})

def add_item(request, rinfo_id):
    rinfo_ = Rinfo.objects.get(id=rinfo_id)
    Bevent.objects.create(blocation=request.POST['bblocation'],bcategory=request.POST['bbcategory'],bdate=request.POST['bbdate'],bbstime=request.POST['bbbstime'],bbetime=request.POST['bbbetime'],bhours=request.POST['bbhours'],bpeople=request.POST['bbpeople'],brates=request.POST['bbrates'],bstat=request.POST['bbstat'],rinfo=rinfo_)
    return redirect(f'/{rinfo_.id}/next')


def info(request):
    return render(request, 'info.html')
def next2(request):
    return render(request, '5model .html')

def bookstatus(request, rinfo_id):
    locations = Location.objects.all()
    rinfo_ = Rinfo.objects.get(id= rinfo_id)
    return render(request, 'bookstatus.html', {'rinfo':rinfo_,'location' : locations
})
def statusupdate(request, rinfo_id):
    rinfo = Bevent.objects.get(id=rinfo_id)
    rinfo.bstatus= request.POST['bbstatus']
    rinfo.save()
    return redirect(f'/{rinfo.id}/bookstatus')
def register(request):
    rinfos = Rinfo.objects.all()
    return render(request, 'register.html', {'rinfos':rinfos})

def bookview(request, rinfo_id):
    locations = Location.objects.all()
    rinfo_ = Rinfo.objects.get(id=rinfo_id)
    return render(request, 'bookview.html', {'rinfo':rinfo_,'location':locations})


def aaccount(request):
    ainfos = Ainfo.objects.all()
    return render(request, 'account.html', {'ainfos':ainfos})

def zad(request):
    if 'next' in request.POST:
        return redirect(request.POST.get('next'))
    else:
        return render(request, 'admin.html')




def adminbook(request):
    rinfos = Rinfo.objects.all()
    return render(request, 'adminbooklist.html', {'rinfos':rinfos})


def add_location(request, id):
  # if request.method=="POST":
   #zlocation = Zlocation.objects.get(id=id)
   zlocation = Zlocation(llocation=request.POST['lllocation'],laddress=request.POST['lladdress'])
   #zlocation.llocation = request.POST['lllocation']
   #zlocation.laddress = request.POST['lladdress']
   #   name=request.POST['name']
     #   age=request.POST['age']
    #    address=request.POST['address']
    #  obj=Details.objects.create(name=name,age=age,address=address)
   zlocation.save()

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
    rinfo.runame = request.POST['vruname']
    rinfo.vage = request.POST['vvage']
    rinfo.vcnumber = request.POST['vvcnumber']
    rinfo.runame = request.POST['vruname']
    rinfo.rpass = request.POST['vrpass']
    rinfo.save()
    return redirect('/')
def delete(request, id):
    rinfo = Rinfo.objects.get(id=id)
    rinfo.delete()
    return redirect('/')
# Create your views here.
def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'index.html')
'''