from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .forms import ContactForm
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class Base_page(generic.TemplateView):
    template_name = 'which_one/index.html'


class Contact_complete_page(generic.TemplateView):
    template_name = 'which_one/cotact_complete.html'

def contact(request):
    form_class = ContactForm(request.POST or None)
    if form_class.is_valid():
        
        contact.name = form_class.cleaned_data['name']
        contact.contact_type = form_class.cleaned_data['contact_type']
        contact.contents = form_class.cleaned_data['contents']

        Contact.objects.create(
            name=contact.name,
            contact_type=contact.contact_type,
            contents=contact.contents,
        )
        return redirect('which_one:complete')
    return render(request, 'which_one/contact.html', {'form': form_class})