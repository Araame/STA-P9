from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Note
class LoginForm (AuthenticationForm):
    username = forms.CharField(
        label="Email",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'xyz@example.com'
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '********'
        })
    )


class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'image', 'category']
    
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    description = forms.CharField(required=False)