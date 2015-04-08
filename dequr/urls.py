from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dequr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('apps.complaint.urls', namespace='complaint')),
    url(r'^', include('apps.general.urls', namespace='general')),
    url(r'^', include('apps.users.urls', namespace='user')),
]
