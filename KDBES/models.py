from django.db import models

#for Registration of Resident
class Rinfo(models.Model):
    rlname = models.TextField(default='')
    rfname = models.TextField(default='')
    rmname = models.TextField(default='')
    raddress = models.TextField(default='')
    rage = models.TextField(default='') 
    rcnumber = models.TextField(default='')
    runame  = models.TextField(default='')
    rpass  = models.TextField(default='')

#for the Event Details
class Bevent(models.Model):
    blocation = models.TextField(default='')
    bcategory = models.TextField(default='')
    bdate = models.TextField(default='')
    bbstime = models.TextField(default='')
    bbetime = models.TextField(default='')
    bhours = models.TextField(default='')
    brates = models.TextField(default='')
    bpeople = models.TextField(default='')
    bstat  = models.TextField(default='')
    rinfo = models.ForeignKey(Rinfo, default="", on_delete = models.CASCADE)

#This model is for Admin view to set the location of a court to be available 
class Zlocation(models.Model):
    llocation = models.TextField(default='')
    laddress = models.TextField(default='')
    bevent = models.ForeignKey(Bevent, default="", on_delete = models.CASCADE)

#This model is for Admin view to Approve and disapprove the request of reservation
class Zremarks(models.Model):
    sremarks = models.TextField(default='') 
    zdate = models.TextField(default='') 
    bevent = models.ForeignKey(Bevent, default="", on_delete = models.CASCADE)

#Model for Admin Log-in
class Areg(models.Model):
    ausername = models.TextField(default='')
    apassword = models.TextField(default='')
