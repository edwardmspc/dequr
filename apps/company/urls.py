from django.conf.urls import include, url
from .views import (CategoryView, CategorysView)


urlpatterns = [
    url(r'^categorys/$', CategorysView.as_view(), name='categorys'),
    url(r'^category/$', CategoryView.as_view(), name='category'),
]
