from django.test import TestCase
from django.urls import reverse, resolve
from which_one.models import Questionnaire, Category
from accounts.models import User
from which_one.views import Index_page, Contact_complete_page, Contact, New_questionnaire_page, Questionnaire_detail_page
import datetime

class TestUrls(TestCase):
  """ページへのURLでアクセスする時のリダイレクトをテスト"""
  # def setUp(self):
  #   """カテゴリー作成"""
  #   Category.objects.create(key=0,name="テスト")
  #   cate = Category.objects.get(key=0)

  #   """ユーザー作成"""
  #   User.objects.create(username="テストユーザー",email="test@test.com")
  #   user = User.objects.get(username="テストユーザー")

  #   """アンケート作成"""
  #   title = "タイトル"
  #   overview = "詳細"
  #   text_A = "テスト"
  #   text_B = "テスト"
  #   category = "ご意見"
  #   questionnaire = Questionnaire.objects.create(user=user, title=title, overview=overview, text_A=text_A, text_B=text_B, category=cate)


  """画面遷移がされることのチェック"""
  def test_Index_page(self):
    view = resolve('/')
    self.assertEqual(view.func.view_class, Index_page)

  def test_Contact(self):
    view = resolve('/contact/')
    self.assertEqual(view.func, Contact)
  
  def test_Contact_complete_page(self):
    view = resolve('/contact/complete/')
    self.assertEqual(view.func.view_class, Contact_complete_page)
  
  def test_New_questionnaire_page(self):
    view = resolve('/new_questionnaire/')
    self.assertEqual(view.func.view_class, New_questionnaire_page)
  
  def test_Questionnaire_detail_page(self):
    view = reverse('which_one:detail',args=[1])
    self.assertEqual( view,'/questionnaire_detail/1/')
