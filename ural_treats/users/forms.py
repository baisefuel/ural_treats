from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-input mail', 'placeholder': 'Ваша почта'})),
    tel = forms.TextInput(attrs={'class': 'form-input tel', 'placeholder': 'Телефон'}),


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
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
