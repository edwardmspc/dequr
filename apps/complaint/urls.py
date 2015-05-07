from django.conf.urls import include, url
from .views import (
                    IndexView,
                    # PostView,
                    #StepOneView,
                    CreateComplaintLastStepView,
                    CategoryView,
                    ProfileView,
                    AjaxCompany,
                    AjaxLoadCategoryFromAutocompleteCompany,
                    AjaxLoadSubCategory,
                    CreateComplaintStepOneWizard,
                    MultiUploadAjax,
                    FORMS
                   )

urlpatterns = [
    url(r'^single_page/$', IndexView.as_view(), name='index'),
    # url(r'^post_page/$', PostView.as_view(), name='create'),
    #url(r'^post_page_step_one/$', StepOneView.as_view(), name='post_step_one_complaint'),
    url(r'^category/$', CategoryView.as_view(), name='category'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),


    #Wizard Create
    url(r'^create_complaint/$', CreateComplaintStepOneWizard.as_view(FORMS, condition_dict={'cc': 0}), name='create'),
    url(r'^create_complaint_last_step/$', CreateComplaintLastStepView.as_view(), name='create_complaint_last_step'),


    #Autocompletar ajax 
    url(r'^ajax_multiupload/$', MultiUploadAjax.as_view(), name='ajax_multiupload'),
    url(r'^ajax_company/$', AjaxCompany.as_view(), name='ajax_company'),
    url(r'^ajax_load_category_from_autocomplete_company/$', AjaxLoadCategoryFromAutocompleteCompany.as_view()),
    url(r'^ajax_load_subcategory/$', AjaxLoadSubCategory.as_view()),
]
