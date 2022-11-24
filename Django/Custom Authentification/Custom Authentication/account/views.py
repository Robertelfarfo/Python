from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MyUserCreationForm

class SingUpView(CreateView):
    form_class = MyUserCreationForm
    success_url= reverse_lazy('login')
    template_name = 'singup.html'
