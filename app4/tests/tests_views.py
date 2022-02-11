from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class RegisterViewTest(TestCase):

    def test1_register_get_form(self):
        url = reverse('register_view')  # auth/register
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')

    def test2_register_post_success(self):
        url = reverse('register_view')
        user_info = {
            'username': 'akbar',
            'password': 'akbar',
            'first_name': 'akbar',
            'last_name': 'babaii',
        }
        response = self.client.post(url, data=user_info)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User registered by ID:")

        self.assertIn(
                user_info['username'],
                list(User.objects.values_list('username', flat=True))
                )
