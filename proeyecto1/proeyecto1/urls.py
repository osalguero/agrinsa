from django.conf.urls import patterns, include, url
from principal.views import index
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proeyecto1.views.home', name='home'),
    # url(r'^proeyecto1/', include('proeyecto1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.STATIC_ROOT,}),
    url(r'^$', index),
)



# tus urlpatterns de toda la vida

