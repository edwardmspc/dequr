from django.conf.urls import include, url
from .views import IndexView


urlpatterns = [
    url(r'^single_page/$', IndexView.as_view(), name='index'),
]
