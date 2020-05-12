# from django import forms
# from django.contrib.auth import authenticate

from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = User
        fields = (
        	'username',
        	'name',
        	'surname',
            'email',
        	'password1',
        	'password2',
        	)


# class UserAuthenticationForm(forms.ModelForm):

# 	password = forms.CharField(label='Password', widget=forms.PasswordInput)

# 	class Meta:
# 		model = User
# 		fields = ('username', 'password')

# 	def clean(self):
# 		if self.is_valid():
# 			# email = self.cleaned_data['email']
# 			password = self.cleaned_data['password']
# 			if not authenticate(password=password):
# 				raise forms.ValidationError("Invalid login")


# class UserUpdateForm(forms.ModelForm):

# 	class Meta:
# 		model = User
# 		fields = ('email', 'username', )

# 	def clean_email(self):
# 		email = self.cleaned_data['email']
# 		try:
# 			User = User.objects.exclude(pk=self.instance.pk).get(email=email)
# 		except User.DoesNotExist:
# 			return email
# 		raise forms.ValidationError('Email "%s" is already in use.' % User)

# 	def clean_username(self):
# 		username = self.cleaned_data['username']
# 		try:
# 			User = User.objects.exclude(pk=self.instance.pk).get(username=username)
# 		except User.DoesNotExist:
# 			return username
# 		raise forms.ValidationError('Username "%s" is already in use.' % username)
















