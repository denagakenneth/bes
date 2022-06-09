from django.urls import include, re_path
from KDBES import views
from django.urls import re_path as url


urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^new$', views.add_item, name='add_item'),    
    url(r'^(\d+)/$', views.view_list, name='view_list'),    
    url(r'^(\d+)/add_info$', views.add_info, name='add_info'),]
    


'''
from django.urls import include, re_path
from django.contrib import admin
from KDBES import views


urlpatterns = [
    re_path(r'^$', views.home_page, name='home_page'),
    re_path(r'^new$', views.new_list, name='new_list'),
    re_path(r'^(\d+)/next$', views.view_list, name='view_list'),
    re_path('admin/', admin.site.urls),
    re_path(r'^(\d+)/add_item$', views.add_item, name='add_item'),
    re_path(r'^login/$', views.Login),
    re_path(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    re_path(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    re_path(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    
    re_path(r'^next2$', views.next2, name='next2'),
    re_path(r'^adminbook/$', views.adminbook, name='adminbook'),
    re_path(r'^zad/$', views.zad, name='zad'),
    re_path(r'^aaccount$', views.aaccount, name='aaccount'),
    re_path(r'^home_log$', views.home_log, name='home_log'),
    re_path(r'^admin_log/$', views.admin_log, name='admin_log'),
    re_path(r'^location$', views.view_location, name='view_location'),
    re_path(r'^add_location$', views.add_location, name='add_location'),
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^(\d+)/next/bookview$', views.bookview, name='bookview'),
    re_path(r'^(\d+)/bookstatus$', views.bookstatus, name='bookstatus'),
    re_path(r'^(\d+)/bookstatus/statusupdate$', views.statusupdate, name='statusupdate'),
    #re_path(r'^index$', views.index, name='index'),
    #re_path(r'^ABOUT$', views.ABOUT, name='ABOUT'),
    #re_path(r'^info$', views.info, name='info'),
]



'''