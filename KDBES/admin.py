from django.contrib import admin
#from KDBES.models import Rinfo,Bevent,Zlocation,Zremarks,Areg
from .models import *

admin.site.register(Rinfo)
admin.site.register(Bevent)
admin.site.register(Zlocation)
admin.site.register(Zremarks)
admin.site.register(Areg)


