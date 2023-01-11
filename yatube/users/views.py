from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class LogoutView(CreateView):
    form_class = LogoutView
    success_url = reverse_lazy('posts:index')
    template_name = 'users/logged_out.html'


class LoginView(CreateView):
    """Кусок кода на удаление"""
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/login.html'
