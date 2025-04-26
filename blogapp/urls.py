#Routes definitions (endpoints) for the blog application    

from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.blog_index, name="blog_index"),
    path("posts/<int:post_id>/", views.blog_detail, name="blog_detail"),
    path("categories/", views.blog_categories, name="blog_categories"),
    path("category/<category>/", views.blog_category, name="blog_category"),
]