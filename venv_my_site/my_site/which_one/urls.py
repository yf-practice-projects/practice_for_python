from django.urls import path, include
from . import views

app_name = 'which_one'
urlpatterns = [
    path(r'', views.Base_page.as_view(),name='base'),
    path(r'contact/', views.contact, name='contact'),
    path(r'complete/', views.Contact_complete_page.as_view(), name='complete'),
]