from django.contrib import admin
from .models import Category, Questionnaire,Choice,Comment,Contact
# Register your models here.
admin.site.register(Category)
admin.site.register(Questionnaire)
admin.site.register(Choice)
admin.site.register(Comment)
admin.site.register(Contact)