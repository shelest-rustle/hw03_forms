from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
# Create your views here.


class Logout(CreateView):
    form_class = CreationForm
    template_name = 'users/logged_out.html'


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
