from django.contrib import admin
from .models import Questionnaire,Comment,Contact,Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Questionnaire)
admin.site.register(Comment)
admin.site.register(Contact)