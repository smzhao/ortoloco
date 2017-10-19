from __future__ import absolute_import, unicode_literals
from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()
from django.contrib.auth.views import login, logout
from django.views.generic import RedirectView
from static_ortoloco import views as static_ortoloco
import juntagrico

import django
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from search import views as search_views

urlpatterns = [
    
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),

    url(r'^search/$', search_views.search, name='search'),

	url('^$', static_ortoloco.home),
	url('^aktuelles$', static_ortoloco.home),
	url('^idee$', static_ortoloco.about),
	url('^portrait$', static_ortoloco.portrait),
	url('^hintergrund$', static_ortoloco.background),
	url('^abo$', static_ortoloco.abo),
	url('^faq$', static_ortoloco.faq),
	url('^mitmachen$', static_ortoloco.join),
	url('^galerie$', RedirectView.as_view(url='/photologue/gallery/page/1/')),
    url('^medien$', static_ortoloco.media),
    url('^links$', static_ortoloco.links),
    url('^dokumente$', static_ortoloco.documents),
    url('^kontakt$', static_ortoloco.contact),
    

    url(r'^', include('juntagrico.urls')),
        
    url(r'^impersonate/', include('impersonate.urls')),

    url(r'^accounts/login/$',  login),


    
    #url('^test_filters/$', my_ortoloco.test_filters),
    #url('^test_filters_post/$', my_ortoloco.test_filters_post),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls)),

    # Uncomment the next line to enable the admin:
    url(r'^django-admin/', include(admin.site.urls)),
    #(r'^tinymce/', include('tinymce.urls')),
    #url(r'^medias/(?P<path>.*)$', django.views.static.serve, {
    #    'document_root': settings.MEDIA_ROOT,
    #}),
	#url(r'^downloads/(?P<param>.*)$', RedirectView.as_view(url='/medias/downloads/%(param)s')),
    #url(r'^static/(?P<path>.*)$', django.views.static.serve, {
    #   'document_root': settings.STATIC_ROOT,
    #})
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

