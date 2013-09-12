from django.conf.urls import patterns, include, url
from fleetimpact.views import homepage, dashboard, thanks


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', homepage),
    url(r'^bienvenu$',homepage),
    url(r'^acceuil$', dashboard),
    url(r'^(w{1,20})\.\acceuil$',dashboard),
    url(r'^exit$', thanks),
    # url(r'^$', 'fleetimpact.views.home', name='home'),
    # url(r'^fleetimpact/', include('fleetimpact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
