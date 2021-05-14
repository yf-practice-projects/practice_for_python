from django.test import TestCase
from django.urls import reverse, resolve
from which_one.models import Questionnaire, Contact, Category
from accounts.models import User

class TestViews(TestCase):
	
	def setUp(self):
		Category.objects.create(key=0,name="テスト")
		User.objects.create(username="テストユーザー",email="test@test.com")
		Questionnaire.objects.create(user=User.objects.get(username="テストユーザー"), title="タイトル", overview = "詳細", text_A = "テスト", text_B = "テスト", category = Category.objects.get(key=0))
	

	def test_New_questionnaire_page(self):
		"""新規作成"""
		response = self.client.get(reverse('which_one:new_questionnaire'))
		self.assertEqual(response.status_code, 200)
		pass

	def test_Index_page(self):
		"""一覧"""
		response = self.client.get(reverse('which_one:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
			response.context['questions_list'],
      		['<Questionnaire: タイトル>'],
      		ordered = False
    	)
		self.assertContains(response, 'タイトル')


	def test_Questionnaire_detail_page(self):
		"""詳細"""
		detail = Questionnaire.objects.get(title="タイトル")
		response = self.client.get(reverse('which_one:detail',args=[detail.id]))
		self.assertEqual(response.status_code, 200)


	def test_Contact(self):
		"""問い合わせ"""
		response = self.client.get(reverse('which_one:contact'))
		self.assertEqual(response.status_code, 200)		


	def test_Contact_complete_page(self):
		"""問い合わせ完了"""
		response = self.client.get(reverse('which_one:complete'))
		self.assertEqual(response.status_code, 200)			

