from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm, NewQuestionnaireForm
from django.forms import formset_factory, modelformset_factory
from .models import Contact,Questionnaire,Category
from accounts.models import User
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

"""一覧ページ"""
class Index_page(generic.ListView):
    context_object_name = 'questions_list'
    model = Questionnaire
    template_name = 'which_one/index.html'

    def get_queryset(self):
        questions = Questionnaire.objects.all().order_by('-created_at')
        return questions


"""問い合わせページ"""
def Contact(request):
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


"""問い合わせ完了ページ"""
class Contact_complete_page(generic.TemplateView):
    template_name = 'which_one/cotact_complete.html'


"""新規作成ページ"""
class New_questionnaire_page(generic.CreateView):
    template_name = 'which_one/new_questionnaire.html'
    # model = Questionnaire
    # fields = ('title','overview','text_A','text_B','image_A','image_B','file_A','file_B','category')
    form_class = NewQuestionnaireForm
    success_url = reverse_lazy('which_one:index')
    
    # def get(self, request):
    #     NewFormSet =  modelformset_factory(Questionnaire, form=NewQuestionnaireForm, extra=2)
    #     if request.method == 'GET':
    #         initial_images = [{'image': i.image, 'image_url': i.image.url} for i in form if i.image]
    #         formset = NewFormSet(initial=initial_images)
    #     return render(request, template_name, {'formset': formset})

    def form_valid(self,form):
        page = form.save(commit=False)
        if self.request.user.is_anonymous:
            gest_user = User.objects.get(pk=1)
            page.user = gest_user
        else:
            page.user = self.request.user
        page.save()
        return super().form_valid(form)


"""詳細ページ"""
class Questionnaire_detail_page(generic.DetailView):
    model = Questionnaire
    template_name = 'which_one/questionnaire_detail.html'
    context_object_name = 'Questionnaire'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post = context.get("object")
    #     # do something
    #     return context
    
    # def get_context_data(self, **kwargs):
    #     context = super(Questionnaire_detail_page, self).get_context_data(**kwargs)
    #     return context

    def post(self,request,pk):
        obj = Questionnaire.objects.get(pk=pk)
        if request.method == "POST":
            if "item-A" == request.POST['accessible-radio']:
                obj.vote_A +=1
                obj.save()
            if "item-B" == request.POST['accessible-radio']:
                obj.vote_B +=1
                obj.save()
            return render(request, 'which_one/questionnaire_detail.html',{'Questionnaire':obj})



def get_client_ip(request):
    '''
    IPアドレスを取得する
    '''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip