""" Views for user app """

from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UsersRegisterForm

class UserRegisterView(CreateView):
    """ Registration view for users """
    template_name = 'users/register.html'
    form_class = UsersRegisterForm
    success_url = '/admin/'
