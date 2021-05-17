from django.test import TestCase
from which_one.models import Questionnaire, Contact, Category
from accounts.models import User

class QuestionnaireTests(TestCase):
    def setUp(self):
        Category.objects.create(key=0,name="テスト")

        """ユーザー作成"""
        User.objects.create(username="テストユーザー",email="test@test.com")

    def test_is_empty(self):
        """初期状態では何も登録されていないことをチェック"""  
        saved_questionnaire = Questionnaire.objects.all()
        self.assertEqual(saved_questionnaire.count(), 0)

    def test_is_count_one(self):
        """1つレコードを適当に作成すると、レコードが1つだけカウントされることをテスト"""
        user = User.objects.get(username="テストユーザー")
        title = "タイトル"
        overview = "詳細"
        text_A = "テスト"
        text_B = "テスト"
        category = Category.objects.get(key=0)

        questionnaire = Questionnaire(user=user, title=title, overview=overview, text_A=text_A, text_B=text_B, category=category)
        questionnaire.save()
        saved_questionnaire = Questionnaire.objects.all()
        self.assertEqual(saved_questionnaire.count(), 1)


class ContactModelTests(TestCase):
    """問い合わせテスト"""
    
    def test_is_empty(self):
        """初期状態では何も登録されていないことをチェック"""  
        saved_posts = Contact.objects.all()
        self.assertEqual(saved_posts.count(), 0)

    def test_is_not_empty(self):
        """初期状態だけど1つはデータが存在しているかどうかをチェック (error が期待される)"""  
        saved_posts = Contact.objects.all()
        self.assertFalse(saved_posts.count(), 1)
    
    def test_is_count_one(self):
        """1つレコードを適当に作成すると、レコードが1つだけカウントされることをチェック"""
        name, contact_type, contents = 'テスト', 0, 'テスト'
        post = Contact(name=name, contact_type=contact_type,contents=contents)
        post.save()
        saved_posts = Contact.objects.all()
        self.assertEqual(saved_posts.count(), 1)
    
    def test_saving_and_retrieving_post(self):
        """内容を指定してデータを保存し、すぐに取り出した時に保存した時と同じ値が返されることをチェック"""
        post = Contact()
        name = 'testuser'
        contact_type = 'ご意見'
        contents = 'テスト'

        post.name = name
        post.contact_type = contact_type
        post.contents = contents
        post.save()

        saved_posts = Contact.objects.all()
        actual_post = saved_posts[0]

        self.assertEqual(actual_post.name, name)
        self.assertEqual(actual_post.contact_type, contact_type)
        self.assertEqual(actual_post.contents, contents)

