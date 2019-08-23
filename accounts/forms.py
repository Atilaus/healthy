from django import forms
from django.contrib.auth.tokens import default_token_generator
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

class PassworResetForm(forms.Form):
	error_messages = {
	'unknown': ("That email address doesn't have an associated "
	"user account. Are you sure you've registered?"),
	'unusable': ("The user account associated with this email "
	"address cannot reset the password."),
	}
	def clean_email(self):

		UserModel = get_user_model()
		email = self.cleaned_data["username"]
		self.users_cache = UserModel._default_manager.filter(username__iexact=username)
		if not len(self.users_cache):
			raise forms.ValidationError(self.error_messages['unknown'])
		if not any(user.is_active for user in self.users_cache):
		# none of the filtered users are active
			raise forms.ValidationError(self.error_messages['unknown'])
		if any((user.password == UNUSABLE_PASSWORD)
		for user in self.users_cache):
			raise forms.ValidationError(self.error_messages['unusable'])
		return email

	def save(self, domain_override=None,
	subject_template_name='registration/password_reset_subject.txt',
	email_template_name='registration/password_reset_email.html',
	use_https=False, token_generator=default_token_generator,
	from_email=None, request=None):
		from django.core.mail import send_mail
		for user in self.users_cache:
			if not domain_override:
				current_site = get_current_site(request)
				site_name = current_site.name
				domain = current_site.domain
			else:
				site_name = domain = domain_override
				c = {
				'email': user.email,
				'domain': domain,
				'site_name': site_name,
				'uid': int_to_base36(user.pk),
				'user': user,
				'token': token_generator.make_token(user),
				'protocol': use_https and 'https' or 'http',
				}
				subject = loader.render_to_string(subject_template_name, c)
				# Email subject *must not* contain newlines
				subject = ''.join(subject.splitlines())
				email = loader.render_to_string(email_template_name, c)
				send_mail(subject, email, from_email, [user.email])