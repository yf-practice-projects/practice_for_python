from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = 'accounts'
urlpatterns = [
    #path(r'login/', views.LoginView.as_view(), name='login'),
    path(r'login/', views.Login_request.as_view() , name='login'),
    path(r'logout/', views.LogoutView.as_view(), name="logout"),
    path(r'profile/',views.ProfileView.as_view(), name='profile'),
    path(r'settings/',views.ProfileView.as_view(), name='settings'),
    path(r'settings/password/',views.ProfileView.as_view(), name='password'),
    path(r'create/', views.UserCreateView.as_view(),name="create"),
    path(r'', include('which_one.urls')),
]