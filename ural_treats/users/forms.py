from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input mail', 'placeholder': 'Ваша почта'}))
    tel = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-input tel', 'placeholder': 'Телефон'}))

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'tel', 'password1', 'password2']
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-input lastName', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input name', 'placeholder': 'Имя'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input pass', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input pass_again', 'placeholder': 'Подтверждение пароля'}),
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.tel = self.cleaned_data['tel']
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Ваша почта'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Ваш пароль'}))

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(('Аккаунт не активен'), code='inactive')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'tel']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input name', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input lastName', 'placeholder': 'Фамилия'}),
            'email': forms.EmailInput(attrs={'class': 'form-input mail', 'placeholder': 'Ваша почта'}),
            'tel': forms.TextInput(attrs={'class': 'form-input tel', 'placeholder': 'Телефон', 'comment': 'Телефон', 'label': 'Телефон'}),
        }
