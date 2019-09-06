from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class SignUpTests(TestCase):
    username = 'testuser'
    email = 'email@.com'

    def test_signup_page_status_code(self):
        res = self.client.get('/accounts/signup/')
        self.assertEqual(res.status_code,200)

    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('custom_account:signup'))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(
            get_user_model().objects.all()[0].username,
            self.username
        )
        self.assertEqual(
            get_user_model().objects.all()[0].email,
            self.email
        )