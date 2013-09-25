from django.conf.urls import patterns, include, url
from fleetimpact.views import homepage, dashboard, thanks, signin, test_maps, test_maps2, test_maps3, test_maps4, homepage2
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', homepage),
    url(r'^bienvenu$',homepage),
    url(r'^acceuil$', dashboard),
    url(r'^(w{1,20})\.\acceuil$',dashboard),
    url(r'^thanks$', thanks),
    url(r'^signin$', signin),
    url(r'^maps$', test_maps),
    url(r'^maps2$', test_maps2),
    url(r'^maps3$', test_maps3),
    url(r'^maps4$', test_maps4),
    url(r'^acceuil2$', homepage2),
    # url(r'^$', 'fleetimpact.views.home', name='home'),
    # url(r'^fleetimpact/', include('fleetimpact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', include('signin.urls', namespace="signin")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^todo/', include('todo.urls', namespace="todo")),
    url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^ecotaxe/', include('ecotaxe.urls', namespace="ecotaxe")),
    url(r'^accounts/', include('registration.backends.default.urls', namespace="accounts")),
    url(r'^$', TemplateView.as_view(template_name = 'index.html'), name='index'),
)
