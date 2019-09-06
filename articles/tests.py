from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Article

class ArticleTest(TestCase):
    username = 'testuser'
    email = 'user@mail.com'
    title = "title of article"
    body = "body of article"

    def test_home_page_status_code(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code,200)

    def test_create_page_status_code(self):
        res = self.client.get('/articles/create')
        self.assertEqual(res.status_code,302)
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.client.force_login(user=user)
        res = self.client.get('/articles/create')
        self.assertEqual(res.status_code,200)
    
    def test_delete_page_status_code(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        w_user = get_user_model().objects.create_user(
            "wrong_user",
            "wrong_email@.com"
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        res = self.client.get('/articles/1/delete')
        self.assertEqual(res.status_code,302)
        self.client.force_login(user=w_user)
        res = self.client.get('/articles/1/delete')
        self.assertEqual(res.status_code,403)
        self.client.logout()
        self.client.force_login(user=user)
        res = self.client.get('/articles/1/delete')
        self.assertEqual(res.status_code,200)

    def test_update_page_status_code(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        w_user = get_user_model().objects.create_user(
            "wrong_user",
            "wrong_email@.com"
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        res = self.client.get('/articles/1/update')
        self.assertEqual(res.status_code,302)
        self.client.force_login(user=w_user)
        res = self.client.get('/articles/1/update')
        self.assertEqual(res.status_code,403)
        self.client.logout()
        self.client.force_login(user=user)
        res = self.client.get('/articles/1/update')
        self.assertEqual(res.status_code,200)

    def test_profile_page_status_code(self):
        res = self.client.get('/articles/profile')
        self.assertEqual(res.status_code,302)
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.client.force_login(user=user)
        res = self.client.get('/articles/profile')
        self.assertEqual(res.status_code,200)

    def test_home_view_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)

    def test_profile_view_by_name(self):
        res = self.client.get(reverse('profile_articles'))
        self.assertEqual(res.status_code,302)
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.client.force_login(user=user)
        res = self.client.get(reverse('profile_articles'))
        self.assertEqual(res.status_code,200)

    def test_create_view_by_name(self):
        res = self.client.get(reverse('article_create'))
        self.assertEqual(res.status_code,302)
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.client.force_login(user=user)
        res = self.client.get(reverse('article_create'))
        self.assertEqual(res.status_code,200)

    def test_delete_view_by_name(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        w_user = get_user_model().objects.create_user(
            "wrong_user",
            "wrong_email@.com"
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        res = self.client.get(reverse('article_delete',args=['1']))
        self.assertEqual(res.status_code,302)
        self.client.force_login(user=w_user)
        res = self.client.get(reverse('article_delete',args=['1']))
        self.assertEqual(res.status_code,403)
        self.client.logout()
        self.client.force_login(user=user)
        res = self.client.get(reverse('article_delete',args=['1']))
        self.assertEqual(res.status_code,200)

    def test_update_view_by_name(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        w_user = get_user_model().objects.create_user(
            "wrong_user",
            "wrong_email@.com"
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        res = self.client.get(reverse('article_update',args=['1']))
        self.assertEqual(res.status_code,302)
        self.client.force_login(user=w_user)
        res = self.client.get(reverse('article_update',args=['1']))
        self.assertEqual(res.status_code,403)
        self.client.logout()
        self.client.force_login(user=user)
        res = self.client.get(reverse('article_update',args=['1']))
        self.assertEqual(res.status_code,200)

    def test_home_view_uses_correct_template(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'home.html')

    def test_profile_view_uses_correct_template(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.client.force_login(user=user)
        res = self.client.get(reverse('profile_articles'))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'articles/profile_articles.html')

    def test_create_view_uses_correct_template(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.client.force_login(user=user)
        res = self.client.get(reverse('article_create'))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'articles/article_create.html')

    def test_delete_view_uses_correct_template(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        self.client.force_login(user=user)
        res = self.client.get(reverse('article_delete',args=['1']))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'articles/article_delete.html')

    def test_update_view_uses_correct_template(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        self.client.force_login(user=user)
        res = self.client.get(reverse('article_update',args=['1']))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'articles/article_update.html')

    def test_create_article_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        self.assertEqual(Article.objects.all().count(),1)
        self.assertEqual(
            Article.objects.all()[0].title,
            self.title
        )
        self.assertEqual(
            Article.objects.all()[0].body,
            self.body
        )
        self.assertEqual(
            Article.objects.all()[0].author,
            user
        )

    def test_update_article_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        Article.objects.create(title=self.title,body=self.body,author = user)
        self.assertEqual(Article.objects.all().count(),1)
        self.assertEqual(
            Article.objects.all()[0].title,
            self.title
        )
        self.assertEqual(
            Article.objects.all()[0].body,
            self.body
        )
        self.assertEqual(
            Article.objects.all()[0].author,
            user
        )
        Article.objects.filter(pk=1).update(title='new title')
        self.assertEqual(
            Article.objects.all()[0].title,
            "new title"
        ) 
