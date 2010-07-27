from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hailpixel.biglist.views.index', name='index'),
    (r'^task/add/$', 'hailpixel.biglist.views.add_task'),
    (r'^task/modify/$', 'hailpixel.biglist.views.modify_task'),
    (r'^complete/$', 'hailpixel.biglist.views.mark_todo_complete'),
    (r'^incomplete/$', 'hailpixel.biglist.views.mark_todo_incomplete'),
    (r'^inbox/$', 'hailpixel.biglist.views.inbox'),
    
    # administration 
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/www/hailpixel/hailpixel-web/biglist/media/'}),
    )