from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
# Create your views here.

class Base_page(generic.TemplateView):
    template_name = 'which_one/index.html'

class Contact_page(generic.FormView):
    template_name = 'which_one/contact.html'
    form_class = ContactForm