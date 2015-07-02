from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login_form.views.home', name='home'),
    # url(r'^login_form/', include('login_form.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','firstproject.views.index',name='index'),
    url(r'^process/$','firstproject.views.process',name='process'),
    url(r'^register/$','firstproject.views.register',name='register'),
)
