from operator import truediv
from django import forms
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm
from django.contrib.auth.models import User
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from crispy_bootstrap5.bootstrap5 import FloatingField

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} existe déjà."),params = {'value':value})

class RegisterForm(SignupForm):
	
	email = forms.EmailField(validators = [validate_email])

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = 'account_signup'
		self.helper.form_method = 'post'
		self.helper.error_text_inline = True 
		self.helper.add_input(Submit('submit', _('Submit'), css_class='btn-primary'))

		self.helper.layout = Layout(FloatingField("username", "email", "password1", "password2"),)

		for field in self.fields:
			help_text = self.fields[field].help_text
			self.fields[field].help_text = None

			if help_text != '':
				self.fields[field].widget.attrs.update({'class':'has-popover', 'title': _('Aide'), 'data-bs-trigger':'hover', 'data-bs-toggle':"popover", 'data-bs-placement':"right", 'data-bs-content':help_text, 'data-placement':'right', 'data-container':'body'})
						
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")			

	def save(self, request):
		user = super(RegisterForm, self).save(request)
		user.email = self.cleaned_data['email']
		user.save()
		return user

class LogForm(LoginForm):

	def __init__(self, *args, **kwargs):
		super(LogForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.error_text_inline = True 
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary rounded-pill btn-sm'))
		self.helper.field_class = 'mb-4'

		for field in self.fields:
			help_text = self.fields[field].help_text
			self.fields[field].help_text = None
			if help_text != '':
				self.fields[field].widget.attrs.update({'class':'has-popover', 'data-bs-trigger':'hover', 'data-bs-toggle':"popover", 'data-bs-placement':"right", 'data-bs-content':help_text, 'data-placement':'right', 'data-container':'body'})		

		self.helper.layout = Layout(FloatingField("login", "password"),)

	def save(self, commit=True):
		user = super(LogForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class CustomResetPasswordForm(ResetPasswordForm):

	def __init__(self, *args, **kwargs):
		super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.error_text_inline = True 
		self.helper.add_input(Submit('submit', _('Reset My Password'), css_class='btn btn-primary rounded-pill btn-sm'))
		self.helper.field_class = 'mb-4'

		for field in self.fields:
			help_text = self.fields[field].help_text
			self.fields[field].help_text = None
			if help_text != '':
				self.fields[field].widget.attrs.update({'class':'has-popover', 'data-bs-trigger':'hover', 'data-bs-toggle':"popover", 'data-bs-placement':"right", 'data-bs-content':help_text, 'data-placement':'right', 'data-container':'body'})		

		self.helper.layout = Layout(FloatingField("email"),)
		
	def save(self, request):
		email_address = super(CustomResetPasswordForm, self).save(request)
		return email_address