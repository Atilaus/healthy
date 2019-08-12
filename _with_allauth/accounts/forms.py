from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model
)
User = get_user_model()

class UserLoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	
	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		
		if email and password:
			user = authenticate(email=email, password=password)
			if not user:
				raise forms.ValidationError('This user does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')
			if not user.is_active:
				raise forms.ValidationError('This user is not active')
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email Address')
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = [
			'email',
			'password'
		]
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError('This email is already being used')
		return email
	