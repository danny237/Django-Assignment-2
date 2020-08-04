""" Registration form for users """

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

USER = get_user_model()

class UsersRegisterForm(UserCreationForm):
    """Custom User Model for registration"""
    class Meta:
        """ using customUsermodel for registration """
        model = USER
        fields = ['username', 'email', 'password1', 'password2']
