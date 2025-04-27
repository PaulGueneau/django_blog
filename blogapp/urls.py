#Routes definitions (endpoints) for the blog application    

from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.blog_index, name="blog_index"),
    path("posts/<int:post_id>/", views.blog_detail, name="blog_detail"),
    path("categories/", views.blog_categories, name="blog_categories"),
    path("category/<category>/", views.blog_category, name="blog_category"),
    path('authors/<str:author_name>/', views.blog_author, name='blog_author'),
    path("authors/", views.blog_authors, name="blog_authors"),
    path("tag/<tag>/", views.blog_tag, name="blog_tag"),
    path("tags/", views.blog_tags, name="blog_tags"),
    path("search/", views.blog_search, name="blog_search"),
]