from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
)

def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authentiicate(email=email, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/')
	
	context = {
		'form': form,
	}
	
	return render(request, 'login.html', context)