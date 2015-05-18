from django.conf.urls import include, url
from .views import IndexView


urlpatterns = [
    url(r'^admin_panel/$', IndexView.as_view(), name='index'),
]
