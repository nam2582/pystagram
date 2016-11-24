from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Post
from .models import Category

class PostTest(TestCase):
    def test_simple(self):
        self.assertEqual(1,1)

    def test_save_post(self):
        category = Category(name='test category')
        category.save()

        post = Post()
        post.category = category
        post.content = 'hello world'
        self.assertIsNone(post.pk)
        post.save()
        self.assertIsNotNone(post.pk)

    def test_failed_to_save_post(self):
        post = Post()
        post.content='test'
        with self.assertRaises(IntegrityError):
            post.save()
