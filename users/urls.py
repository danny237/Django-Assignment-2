""" Urls for users app """

from django.urls import path
from . import views as auth_views

urlpatterns = [
    # users/
    path('create/', auth_views.UserRegisterView.as_view(), name='register')
]
