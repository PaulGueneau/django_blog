from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from blogapp.models import Post, Category, Author, Comment
from blogapp.forms import CommentForm
from django.urls import reverse

# Test cases for models 

class PostModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
        )
        self.post.categories.set([self.category])  #many-to-many relationships

    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.categories.first().name, "Test Category")  # Access the category's name


class CategoryModelTest(TestCase):
        def setUp(self):
           self.category = Category.objects.create(
            name = "Category 1"
           )

        def test_category_creation(self):
            self.assertEqual(self.category.name, "Category 1")



    

# Test cases for views 

class BlogIndexViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
        )
        self.post.categories.set([self.category])  #many-to-many relationships

    def test_blog_index_view(self):
        response = self.client.get(reverse('blog_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/index.html')
        self.assertContains(response, "Test Post")


# class CategoriesViewTest(TestCase):



# Test cases for forms 


# Test cases for the API 