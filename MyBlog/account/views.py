from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from account.forms import RegisterForm, LoginForm


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'account/registration_form.html'

    def form_valid(self, form):
        user = form.save(False)

        user.save(True)
        return HttpResponseRedirect('/')

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'