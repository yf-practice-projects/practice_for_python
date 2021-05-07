from django.db import models
from accounts.models import User
# Create your models here.

"""ユーザー投稿"""
class Category(models.Model):
    class Meta:
        verbose_name = "カテゴリー"
        verbose_name_plural = "カテゴリー"

    key = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='カテゴリー', max_length=20)
    
    def __str__(self):
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
    image_A = models.ImageField(verbose_name='質問画像_A', blank=True, upload_to='images/',)
    image_B = models.ImageField(verbose_name='質問画像_B', blank=True, upload_to='images/',)
    file_A = models.FileField(verbose_name='質問音声_A', blank=True)
    file_B = models.FileField(verbose_name='質問音声_B', blank=True)
    category = models.ForeignKey(
                    Category, verbose_name='カテゴリー',
                    to_field='key',
                    on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    vote_A = models.IntegerField(default=0)
    vote_B = models.IntegerField(default=0)

    def __str__(self):
        return self.title


'''第三者投稿'''
# class ChoiceManager(models.Manager):
#     def create_choice(self,ip_address,questionnaire_id):
#         choice = self.model(  
#             questionnaire_id=questionnaire_id,
#             ip_address=ip_address,
#         )
#         try:
#             choice.save()
#         except:
#             return False
#         return True

class Choice(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    ip_address = models.CharField(
        'IPアドレス',
        max_length=50,
        default=0,
    ) 
    vote_A = models.IntegerField(default=0)
    vote_B = models.IntegerField(default=0)
    # objects = ChoiceManager()
    
    def __str__(self):
        return self.questionnaire.title

class Comment(models.Model):
    class Meta:
        verbose_name = 'コメント'
    
    name = models.CharField('名前', max_length=20, default='名無し')
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='コメント',blank=False)
    created_date = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    
    def __str__(self):
        return self.text
    


"""問い合わせ"""
class Contact(models.Model):
    class Meta:
        verbose_name = 'お問い合わせ'
    
    name = models.TextField(verbose_name='お名前', blank=False, max_length=15)
    contact_type = models.TextField(verbose_name='種類', blank=False)
    contents = models.TextField(verbose_name='お問い合わせ内容')

    def __str__(self):
        return self.name