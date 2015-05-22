from django.conf.urls import include, url
from .views import IndexView, ParentView, AJAXChangeCategoryView, AJAXChangeSubCategoryView, AJAXChangeEmailView, AJAXChangeFacebookView, AJAXChangeTwitterView, AJAXChangeWebUrlView, AJAXChangePhoneView, AJAXCompanyActivateView


urlpatterns = [
    url(r'^moderate_children/$', IndexView.as_view(), name='index'),
    url(r'^moderate_parent/$', ParentView.as_view(), name='parent'),
    url(r'^AJAX_change_category/$', AJAXChangeCategoryView.as_view(), name='AJAX_change_category'),
    url(r'^AJAX_change_subcategory/$', AJAXChangeSubCategoryView.as_view(), name='AJAX_change_category'),
    url(r'^AJAX_change_email/$', AJAXChangeEmailView.as_view(), name='AJAX_change_email'),
    url(r'^AJAX_change_phone/$', AJAXChangePhoneView.as_view(), name='AJAX_change_phone'),
    url(r'^AJAX_change_web_url/$', AJAXChangeWebUrlView.as_view(), name='AJAX_change_web_url'),
    url(r'^AJAX_change_twitter/$', AJAXChangeTwitterView.as_view(), name='AJAX_change_twitter'),
    url(r'^AJAX_change_facebook/$', AJAXChangeFacebookView.as_view(), name='AJAX_change_facebook'),
    url(r'^AJAX_company_activate/$', AJAXCompanyActivateView.as_view(), name='AJAX_company_activate'),
]
