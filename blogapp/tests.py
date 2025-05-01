from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from blogapp.models import Post, Category, Author, Comment, Tag
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


class CommentModelTest(TestCase):
        def setUp(self):
            self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
           )
            self.comment = Comment.objects.create(
                body='This is a comment',
                author='Author1',
                post=self.post
                )
          
        def test_comment_creation(self):
            self.assertEqual(self.comment.body, "This is a comment")
            self.assertEqual(self.comment.post.title, "Test Post")
            self.assertEqual(self.comment.author, 'Author1')
            

class AuthorModelTest(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(   
            title="Test Post 1",
            content="This is the first test post.",
        )
        self.post2 = Post.objects.create(
            title="Test Post 2",
            content="This is the second test post.",
        )
        self.author = Author.objects.create(
            name="Author 1",
            email="author@gmail.com",
            bio="This is a test author."
        )
        self.author.posts.set([self.post1, self.post2])  # many-to-many relationships

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Author 1")
        self.assertEqual(self.author.email, "author@gmail.com")
        self.assertEqual(self.author.bio, "This is a test author.")
        self.assertEqual(self.author.posts.count(), 2)
        self.assertEqual(self.author.posts.first().title, "Test Post 1")
        self.assertEqual(self.author.posts.last().title, "Test Post 2")


class TagModelTest(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            title="Test Post 1",
            content="This is the first test post.",
        )
        self.post2 = Post.objects.create(
            title="Test Post 2",
            content="This is the second test post.",
        )
        self.tag = Tag.objects.create(name="Tag 1")
        self.tag.posts.set([self.post1,self.post2])  # many-to-many relationships

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Tag 1")
        self.assertEqual(self.tag.posts.first().title, "Test Post 1")
        self.assertEqual(self.tag.posts.last().title, "Test Post 2")


### Test cases for forms ####
class CommentFormTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
        )
        self.form_data = {
            'author': 'Comment Author',
            'body': 'This is a test comment.',
        }
        self.form = CommentForm(data=self.form_data)

    def test_form_valid(self):
        self.assertTrue(self.form.is_valid())

    def test_form_invalid_empty_fields(self):
        invalid_data = {
            'author': '',
            'body': '',
        }
        form = CommentForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_author_too_long(self):
        invalid_data = {
            'author': 'Comment Author with a very long name that exceeds the max length',
            'body': 'Body of the comment',
        }
        form = CommentForm(data=invalid_data)
        self.assertFalse(form.is_valid())   

    

### Test cases for views ####

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

class CategoriesViewTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Test Category")
        self.category2 = Category.objects.create(name="Another Category")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
        )
        self.post.categories.set([self.category1, self.category2])  #many-to-many relationships


    def test_blog_categories_view(self):
        response = self.client.get(reverse('blog_categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/categories.html')
        self.assertContains(response, "Test Category")
        self.assertContains(response, "Another Category")

class CategoryViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.post1 = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
        )
        self.post2 = Post.objects.create(
            title="Another Test Post",
            content="This is another test post.",
        )
        self.post1.categories.set([self.category])  #many-to-many relationships
        self.post2.categories.set([self.category])

    def test_blog_category_view(self):
        response = self.client.get(reverse('blog_category', args=[self.category.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/category.html')
        self.assertContains(response, "Test Post")
        self.assertContains(response, "Another Test Post")

class BlogDetailViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
        )
        self.post.categories.set([self.category])  #many-to-many relationships
        self.comment = Comment.objects.create(
            body='This is a comment',
            author='Author1',
            post=self.post
        )

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/detail.html')
        self.assertContains(response, "Test Post")
        self.assertContains(response, "This is a comment")
        self.assertContains(response, "Author1")

    def test_blog_detail_view_post_comment(self):
        response = self.client.post(reverse('blog_detail', args=[self.post.id]), {
            'author': 'New Author',
            'body': 'This is a new comment.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('blog_detail', args=[self.post.id]))
        self.assertTrue(Comment.objects.filter(body='This is a new comment.').exists())


class BlogAuthorViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.post1 = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
        )
        self.post2 = Post.objects.create(
            title="Another Test Post",
            content="This is another test post.",
        )
        self.author = Author.objects.create(
            name="Author 1",
            email="author@email.com",
            bio="This is a test author."
        )
        self.author.posts.set([self.post1, self.post2])
        self.post1.authors.set([self.author])
        self.post2.authors.set([self.author])

    def test_blog_author_view(self):
        response = self.client.get(reverse('blog_author', args=[self.author.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogapp/author.html')
        self.assertContains(response, "Author 1")
        self.assertContains(response, "Test Post")
        self.assertContains(response, "Another Test Post")

