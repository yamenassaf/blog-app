from django.test import TestCase
from .models import Post

# Create your tests here.

class TestHomePageView(TestCase):
	def setUp(self):
		Post.objects.create(title='just a test',author=)
	def test_text_content(self):
		post=Post.objects.get(id=1)
		assertEqual(post.title, 'just a test')