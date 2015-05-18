from django.conf.urls import include, url
from django.contrib import admin
import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'dequr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('apps.adminpanel.urls', namespace='panel')),
    url(r'^', include('apps.category.urls', namespace='category')),
    url(r'^', include('apps.company.urls', namespace='company')),
    url(r'^', include('apps.complaint.urls', namespace='complaint')),
    url(r'^', include('apps.general.urls', namespace='general')),
    url(r'^', include('apps.users.urls', namespace='user')),

]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    ]

