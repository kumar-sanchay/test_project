from django import forms
from django.contrib.auth.models import User
from .models import Post


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Re-enter Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password didn\'t match !!')
        return cd['password1']


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['text']