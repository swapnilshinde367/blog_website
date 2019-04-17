from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . forms import CustomUserCrationForm

def register( request ) :

	if request.method == 'POST' :
		form = CustomUserCrationForm( request.POST )

		if form.is_valid() :
			user = form.save()
			username = form.cleaned_data.get( 'username' )
			messages.success( request, f"Account for {username} is created successfully!!" )
			login( request, user )
			messages.success( request, f"Logged in as {username}" )
			return redirect( "blogs_home" )
		else :
			for error in form.error_messages :
				messages.error( request, f"{error}" )

	form = CustomUserCrationForm()
	context = { 'title' : 'Registration',
				'form' : form}
	return render( request = request,
					template_name = "users/register.html",
					context = context )

@login_required
def user_profile( request ) :
	return render( request = request,
					template_name = 'users/profile.html' )