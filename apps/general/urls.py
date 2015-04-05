from django.conf.urls import include, url
from .views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]


from django.conf import settings
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    ]