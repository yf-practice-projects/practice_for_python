from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django import forms

User = get_user_model()

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = "username"        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = "email"
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = "Password"
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("正しいメールアドレスを指定して下さい。")
 
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise ValidationError("このメールアドレスは既に使用されています。別のメールアドレスを指定してください")

# class LoginForm(AuthenticationForm):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), min_length=8)
