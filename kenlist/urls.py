from django.urls import re_path as url
from django.contrib import admin
from KDBES import views
from django.conf.urls import include
#from django.conf import settings


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^home_log$', views.home_log, name='home_log'),
    url(r'^login/$', views.Login),
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/next$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),

    url('admin/', admin.site.urls),
    url(r'^adminbook/$', views.adminbook, name='adminbook'),
    url(r'^admin_log/$', views.admin_log, name='admin_log'),
    url(r'^aaccount$', views.aaccount, name='aaccount'),
    url(r'^(\d+)/eventstatus$', views.eventstatus, name='eventstatus'),
    url(r'^(\d+)/eventstatus/statusupdate$', views.statusupdate, name='statusupdate'),

    url(r'^register$', views.register, name='register'),
    url(r'^(\d+)/next/eventview$', views.eventview, name='eventview'),
    
    url(r'^location$', views.view_location, name='view_location'),
    url(r'^add_location$', views.add_location, name='add_location'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^Schedule$', views.Schedule, name='Schedule'),

    url(r'^zad/$', views.zad, name='zad'),
    #url(r'^index$', views.index, name='index'),
    #url(r'^next2$', views.next2, name='next2'),
    #url(r'^info$', views.info, name='info'),
]



'''

from django.urls import include, re_path
from KDBES import views
from django.urls import re_path as url


urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^new$', views.add_item, name='add_item'),    
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^register$', views.register, name='register'),    
    url(r'^(\d+)/add_info$', views.add_info, name='add_info'),]
    







































'''







