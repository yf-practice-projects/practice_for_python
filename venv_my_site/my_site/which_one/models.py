from django.db import models
from accounts.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリー', max_length=20)
    
    def __str__():
        return self.name

class Questionnaire(models.Model):
    class Meta:
        verbose_name = 'アンケート'
        verbose_name_plural = 'アンケート'
    
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    overview = models.TextField(verbose_name='概要', blank=False)
    text_A = models.TextField(verbose_name='質問文_A', blank=True)
    text_B = models.TextField(verbose_name='質問文_B', blank=True)
    image_A = models.ImageField(verbose_name='質問画像_A', blank=True)
    image_B = models.ImageField(verbose_name='質問画像_B', blank=True)
    file_A = models.ImageField(verbose_name='質問音声_A', blank=True)
    file_B = models.ImageField(verbose_name='質問音声_B', blank=True)
    category = models.ForeignKey(
                    Category, verbose_name='カテゴリー',
                    on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Comment(models.Model):
    class Meta:
        verbose_name = 'コメント'

    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='コメント',blank=False)
    created_date = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
            
    def __str__(self):
        return self.text
    

class Contact(models.Model):
    class Meta:
        verbose_name = 'お問い合わせ'
    
    name = models.TextField(verbose_name='お名前', blank=False, max_length=15)
    contact_type = models.TextField(verbose_name='種類', blank=False)
    contents = models.TextField(verbose_name='お問い合わせ内容')
    
    def __str__(self):
        return self.name