from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UsersViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user = User.objects.create_user(username = "testuser", email = "testuser@example.com", password = "password")

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        # Test Post Request
        response = self.client.post(self.register_url, {'username': 'newuser', 'email': 'newuser@example.com', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username = "testuser", password = "password")
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        # Test Post Request
        with open("static/images/default.jpg", 'rb') as image_file:
            response = self.client.post(self.profile_url, {'image': image_file})
        self.assertEqual(response.status_code, 200)
        response = self.client.post(self.profile_url, {"username" : "NewUser","email" : "newtestuser@example.com"})
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        # Test Post Request
        response = self.client.post(self.login_url, {'username' : 'testuser', 'password' : "password" })
        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
