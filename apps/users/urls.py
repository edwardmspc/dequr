from django.conf.urls import include, url
from .views import LoginIndex, LogoutView, RequiredEmailView


urlpatterns = [
    url(r'^login_o_registro/$', LoginIndex.as_view(), name='index'),
    url(r'^required_email/$', RequiredEmailView.as_view(), name='required_email'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
