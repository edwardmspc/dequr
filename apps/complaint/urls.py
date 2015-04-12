from django.conf.urls import include, url
from .views import IndexView, PostView, StepOneView, StepTwoView


urlpatterns = [
    url(r'^single_page/$', IndexView.as_view(), name='index'),
    url(r'^post_page/$', PostView.as_view(), name='post_complaint'),
    url(r'^post_page_step_one/$', StepOneView.as_view(), name='post_step_one_complaint'),
    url(r'^post_page_step_two/$', StepTwoView.as_view(), name='post_step_two_complaint'),
]
