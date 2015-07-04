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
    url(r'^process1/(?P<pk>\d+)/$', 'firstproject.views.userprofileedit',name='userprofileedit'),
    url(r'^register/$','firstproject.views.register',name='register'),
    # url(r'^savechanges/$','firstproject.views.savechanges',name='savechanges'),
    url(r'^save/(?P<pk>\d+)$','firstproject.views.save',name='save'),
    url(r'^logout/$','firstproject.views.logout',name='logout'),
    url(r'^change_password/$','firstproject.views.reset',name='reset'),
    url(r'^success/$','firstproject.views.success',name='success'),
    url(r'^product_detail/$', 'product.views.product_detail', name='product_detail'),
    url(r'^submitquery/$', 'product.views.save',name='product_save'),
    url(r'^details/$', 'product.views.details',name="details"),
    url(r'^particular_details/(?P<pk>\d+)/$', 'product.views.particular_details',name="particular_details"),

    
)
