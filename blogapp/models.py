from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #one post can have many comments and if the post is deleted, the comments are also deleted
    body = models.TextField(default='')
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'


class Author(models.Model):     
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
    posts = models.ManyToManyField(Post, related_name='authors')

    def __str__(self):
        return self.name

    
class Tag(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post, related_name='tags')
    class Meta:
        verbose_name_plural = "tags"
    
    def __str__(self):
        return self.name