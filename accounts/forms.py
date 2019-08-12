from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model
)
User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField(label='Email',
	widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
	#password = forms.CharField(widget=forms.PasswordInput)
	next = forms.CharField(widget=forms.HiddenInput(), required=False)
	#add
	class Meta:
		model=User
		fields=('username', 'password')
	
	def clean(self, *args, **kwargs):

		
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('Incorrect email or password')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')
			if not user.is_active:
				raise forms.ValidationError('This user is not active')
				
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	username = forms.EmailField(label='Email',
	widget=forms.EmailInput(attrs={'class': 'form-control'}))

	password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}))
	
	class Meta:
		model = User
		fields = [
			'username',
			'password'
		]
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			raise forms.ValidationError('This email is already being used')
		return username
	