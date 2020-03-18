from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from .models import Users


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required. Add a valid email')

    class Meta:
        model = Users
        fields = ('email','username','password1','password2',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = Users.objects.exclude(pk=self.instance.pk).get(email=email)
        except Users.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.'% user)


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model = Users
        fields = ('email','password')
    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError('Invalid login')
