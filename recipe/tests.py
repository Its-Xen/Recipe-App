from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Post

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Desserts")

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name="Desserts")
        self.post = Post.objects.create(
            author=self.user,
            recipe="Chocolate Cake",
            category=self.category,
            desc="Delicious chocolate cake recipe."
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), "Chocolate Cake")

