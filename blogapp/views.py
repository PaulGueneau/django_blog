from django.shortcuts import render
from blogapp.models import Post, Comment, Author, Category, Tag
from blogapp.forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Q  # Import Q for complex queries
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
    query = request.GET.get("q")  # Get the search query from the request
    if query:
        posts = Post.objects.filter(title__icontains=query).order_by("-created_at")  # Filter posts by title containing the query
    else:
        posts = Post.objects.all().order_by("-created_at")  # Fetch all posts if no query is provided
    context = {
        "posts": posts,
        "query": query,  # Pass the query back to the template to display in the search bar
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

    # View to handle posts by author
def blog_author(request, author_name):
    author = Author.objects.get(name=author_name)  
    posts = Post.objects.filter(authors=author).order_by("-created_at")  
    context = {
        "author": author,
        "posts": posts,
        }
    return render(request, "blogapp/author.html", context)

def blog_authors(request):
    authors = Author.objects.all()  # Fetch all authors from the database
    context = {
        "authors": authors,
    }
    return render(request, "blogapp/authors.html", context)
    

    # View to handle posts by specific tag
def blog_tag(request, tag):
    tag_obj = Tag.objects.get(name=tag)  # Fetch the tag with the given name
    posts = Post.objects.filter(tags=tag).order_by("-created_at")  # Fetch all posts with the tag
    context = {
        "tag": tag_obj,
        "posts": posts,
    }
    return render(request, "blogapp/tag.html", context)
    
# View to handle all tags
def blog_tags(request):
    tags = Tag.objects.all()  # Fetch all tags from the database
    context = {
        "tags": tags,
    }
    return render(request, "blogapp/tags.html", context)



    # View to handle search functionality
def blog_search(request):
    query = request.GET.get("q", "")  # Get the search query from the request
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by("-created_at") if query else []  # Search posts by title or content
    context = {
        "query": query,
        "posts": posts,
        }
    return render(request, "blogapp/search.html", context)