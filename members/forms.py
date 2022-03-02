from operator import truediv
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Button
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} existe déjà."),params = {'value':value})

class RegisterForm(UserCreationForm):
	
	email = forms.EmailField(validators = [validate_email])

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.error_text_inline = True 
		self.helper.add_input(Submit('submit', _('Submit'), css_class='btn-primary'))

		for field in self.fields:
			help_text = self.fields[field].help_text
			self.fields[field].help_text = None
			if help_text != '':
				self.fields[field].widget.attrs.update({'class':'has-popover', 'data-bs-trigger':'hover', 'data-bs-toggle':"popover", 'data-bs-placement':"right", 'data-bs-content':help_text, 'data-placement':'right', 'data-container':'body'})
						
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")			

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LoginForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'post'
		self.helper.error_text_inline = True 
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

		for field in self.fields:
			help_text = self.fields[field].help_text
			self.fields[field].help_text = None
			if help_text != '':
				self.fields[field].widget.attrs.update({'class':'has-popover', 'data-bs-trigger':'hover', 'data-bs-toggle':"popover", 'data-bs-placement':"right", 'data-bs-content':help_text, 'data-placement':'right', 'data-container':'body'})		

	def save(self, commit=True):
		user = super(LoginForm, self).save(commit=False)
		if commit:
			user.save()
		return user
