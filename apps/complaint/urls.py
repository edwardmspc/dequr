from django.conf.urls import include, url
from .views import IndexView, PostView


urlpatterns = [
    url(r'^single_page/$', IndexView.as_view(), name='index'),
    url(r'^post_page/$', PostView.as_view(), name='post_complaint'),
]
