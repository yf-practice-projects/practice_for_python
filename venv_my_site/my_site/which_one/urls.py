from django.urls import path, include
from . import views

app_name = 'which_one'
urlpatterns = [
    path(r'questionnaire_detail/<int:pk>/', views.Questionnaire_detail_page.as_view(), name='detail'),
    path(r'', views.Index_page.as_view(),name='index'),
    path(r'contact/', views.Contact_page, name='contact'),
    path(r'contact/complete/', views.Contact_complete_page.as_view(), name='complete'),
    path(r'new_questionnaire/', views.New_questionnaire_page.as_view(), name='new_questionnaire'),
    
]