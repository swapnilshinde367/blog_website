from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . models import Profile

class CustomUserCrationForm( UserCreationForm ) :
	email = forms.EmailField()

	class Meta :
		model = User
		fields = [ 'username', 'email', 'password1', 'password2' ]


class UserUpdateProflile( forms.ModelForm ) :
	email = forms.EmailField()

	class Meta :
		model = User
		fields = [ 'username', 'email' ]

class ProfileUpdateImageForm( forms.ModelForm ) :
	class Meta :
		model = Profile
		fields = ['user_image']