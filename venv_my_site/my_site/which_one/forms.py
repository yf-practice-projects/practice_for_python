from django import forms
from .models import Contact

class ContactForm(forms.Form):

    # class Meta:
    #     model = Contact
    #     fields = ('name','contact_type','contents')

    CHOICES = (
    ("0", "ご意見"),
    ("1", "ご報告"),
    ("2", "その他")
    )

    name = forms.CharField(label='お名前',
                max_length=15,
            )
            
    contact_type = forms.ChoiceField(label='お問い合わせの種類',
                                widget=forms.Select, 
                                choices=CHOICES  # リストを指定する
                    )
    contents = forms.CharField(label='お問い合わせ内容',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-12 my-3'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前'

        self.fields['contact_type'].widget.attrs['class'] = 'form-control col-12 my-3'

        self.fields['contents'].widget.attrs['class'] = 'form-control col-12 my-3'
        self.fields['contents'].widget.attrs['placeholder'] = 'お問い合わせ内容はこちら'
    
    def save():
        pass
