from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'hailpixel.biglist.views.index'),
    
    #static media
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/www/hailpixel/hailpixel-web/biglist/media/'}),
    
    # administration 
    (r'^admin/', include(admin.site.urls)),
)