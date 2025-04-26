from django.shortcuts import render
from blogapp.models import Post, Comment, Author, Category, Tag
from blogapp.forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.


def blog_categories(request):
    categories = Category.objects.all() # Fetch all categories from the database
    context = {
        "categories": categories,
    }
    return render(request, "blogapp/categories.html", context)

#Equivalent to a GET request to /blog/category/<category>/
# This view fetches all posts that belong to a specific category
def blog_category(request, category):
    # Fetch the category object with the given name
    category_obj = Category.objects.get(name=category)
    # Fetch all posts that belong to this category
    posts = Post.objects.filter(categories=category_obj).order_by("-created_at")
    context = {
        "posts": posts,
        "category": category_obj,
    }
    return render(request, "blogapp/category.html", context)

#Equivalent to a GET request to all the posts in the blog
def blog_index(request):
    posts = Post.objects.all().order_by("-created_at") # Fetch all posts and order them by creation date in descending order
    context = {
        "posts": posts,
    }
    return render(request, "blogapp/index.html", context)

def blog_detail(request, post_id):
    post = Post.objects.get(id=post_id) # Fetch the post with the given ID
    form = CommentForm() # Create an instance of the CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save() # Save the comment to the database
            return HttpResponseRedirect(request.path) # Redirect to the same page to avoid resubmission
    comments = Comment.objects.filter(post=post) # Fetch all comments related to the post
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blogapp/detail.html", context)

#Equivalent to a POST request to /blog/create/
# This view handles the creation of a new blog post
def blog_create(request):
    if request.method == "POST":
        # Get the title and content from the POST request
        title = request.POST.get("title")
        content = request.POST.get("content")
        # Create a new post with the provided title and content
        post = Post.objects.create(title=title, content=content)
        # Redirect to the detail view of the newly created post
        return redirect("blog_detail", post_id=post.id)

# Equivalent to a PUT request to /blog/update/<post_id>/
# def blog_update(request, post_id):
#     # Fetch the post with the given ID
#     post = Post.objects.get(id=post_id)
#     if request.method == "PUT":
#         # Get the updated title and content from the PUT request
#         title = request.POST.get("title")
#         content = request.POST.get("content")
#         # Update the post's title and content
#         post.title = title
#         post.content = content
#         # Save the updated post to the database
#         post.save()
#         # Redirect to the detail view of the updated post
#         return redirect("blog_detail", post_id=post.id)
#     # Pass the post to the update template for rendering
#     context = {
#         "post": post,
#     }
#     return render(request, "blog/update.html", context)


# def blog_delete(request, post_id):
#     post = Post.objects.get(id=post_id) # Fetch the post with the given ID
#     if request.method == "DELETE":
#         post.delete() # Delete the post
#         return redirect("blog_index") # Redirect to the index view
#     context = {
#         "post": post,
#     }
#     return render(request, "blog/delete.html", context)