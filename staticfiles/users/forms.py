from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth import get_user_model
User=get_user_model()

class LoginForm(forms.Form):
    username=forms.CharField(max_length=65, widget=forms.TextInput(attrs={
        'placeholder':'Enter username',
        'class':'px-6 py-4 border border-gray-700 rounded-xl w-full mb-2'

    }))
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':'px-6 py-4 border border-gray-700 rounded-xl w-full mb-2'

    }))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2',]
    username=forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Enter Username',
            'class':'w-full px-6 py-4 rounded-xl border border-gray-700'
        }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter email Address',
        'class':'w-full px-6 py-4 rounded-xl border border-gray-700'
    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'w-full px-6 py-4 rounded-xl border border-gray-700'

    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password',
        'class':'w-full px-6 py-4 rounded-xl border border-gray-700'

    }))

    def clean_password(self):
        cd=self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password did not match')
        return cd['password2']
    
    def clean_email(self):
        data=self.cleaned_data['email']
        qs=User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError("Email is already in use !!!!")
        return data