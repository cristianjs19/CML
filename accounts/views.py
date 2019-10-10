from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from accounts.forms import RegistrationForm
from .models import Account


class AccountCreateView(CreateView):
	template_name = 'form.html'
	form_class = RegistrationForm
	extra_context={'title':'Register'}
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(AccountCreateView, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context


	def post(self, request, *args, **kwargs):
			self.object = self.get_object
			form = self.form_class(request.POST)
			if form.is_valid():
				account = form.save()
				account.save()
				# email = form.cleaned_data.get('email')
				username = form.cleaned_data.get("username")
				raw_password = form.cleaned_data.get('password1')
				account = authenticate(username=username, password=raw_password)
				login(request, account)
				return HttpResponseRedirect(self.get_success_url())
			else:
				return self.render_to_response(self.get_context_data(form=form))
		