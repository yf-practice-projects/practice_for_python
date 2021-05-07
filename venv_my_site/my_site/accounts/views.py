
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView
from django.contrib.auth import login,authenticate
from django.urls import reverse_lazy
from django.views import generic
from . import forms

# class LoginView(LoginView):
#     form_class = forms.LoginForm
#     template_name = "accounts/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "accounts/logout.html"

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)

class UserCreateView(CreateView):
    form_class = forms.UserCreationForm
    template_name = "accounts/create.html"
    success_url = reverse_lazy("which_one:index")

class SettingsView():
    pass

class PassChangeView():
    pass


class Login_request(generic.FormView):
    params = {'username':'','password':''}
    template_name = "accounts/login.html"
    form_class = forms.LoginForm

    def form_valid(self,form):
        params["username"] = form.data.get("username")
        params["password"] = form.data.getlist("password")
        return super().form_valid(form)

    def post(self, request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('which_one:index')
                else:
                    return render(request, 'accounts/login.html', {'error':'社員名かパスワードが間違っています'})
            else:
                return render(request, 'accounts/login.html', {'error':'ユーザーを入力してください'})