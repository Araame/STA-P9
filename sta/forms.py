from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Note

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2.5 px-3 border-muted-subtle',
        'placeholder': 'Enter your username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2.5 px-3 border-muted-subtle',
        'placeholder': 'Enter your password'
    }))



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'category', 'image']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control py-2.5 px-3 border-muted-subtle',
                'placeholder': 'Title *'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control px-3 py-2 border-muted-subtle',
                'rows': 4,
                'placeholder': 'Description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select py-2.5 px-3 border-muted-subtle'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control py-2.5 px-3 border-muted-subtle',
                'placeholder': 'Title *'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control px-3 py-2 border-muted-subtle',
                'rows': 4,
                'placeholder': 'Description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select py-2.5 px-3 border-muted-subtle'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }
    
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    description = forms.CharField(required=False)