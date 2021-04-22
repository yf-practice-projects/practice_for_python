from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
from .models import Contact
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class Base_page(generic.TemplateView):
    template_name = 'which_one/index.html'

class Contact_page(generic.FormView):
    template_name = 'which_one/contact.html'
    form_class = ContactForm
    reverse_lazy('which_one:complete')

    def form_valid(self, form):
        form.save()  # 保存処理など
        messages.add_message(self.request, messages.SUCCESS, 'ご連絡ありがとうございます。')  # メッセージ出力
        return super().form_valid(form)