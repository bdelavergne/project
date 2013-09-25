from django.conf.urls import patterns, url

from todo import views

urlpatterns = patterns('',
    url(r'^mark_done/(\d*)/$', "views.mark_done"),
   
)
