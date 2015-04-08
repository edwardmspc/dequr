from django.conf.urls import include, url
from .views import IndexView


urlpatterns = [
    url(r'^ddd/$', IndexView.as_view(), name='sss'),
]
