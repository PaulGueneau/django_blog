## A full-featured blog application built with Django that allows users to create, edit, and interact with blog posts.

*Features* 

- User authentication system (register, login, logout) -> TBD 
- User profiles with profile pictures -> TBD
- Create, update, and delete blog posts
- Pagination for blog posts -> TBD 
- Comment system for blog posts
- Category and tag filtering

**Installation**

1. Clone the repository:

`git clone https://github.com/yourusername/django-blog.git`

`cd django-blog`

2. Create and activate a virtual environment:

`python (or python3) -m venv venv`

`source venv/bin/activate`

On Windows: `venv\Scripts\activate`

3. Install required packages:

`pip install -r requirements.txt`

4. Run migrations:

`python manage.py migrate`

5. Create a superuser:

`python manage.py createsuperuser`

6. Run the development server:

`python manage.py runserver`

7. Access the app at http://localhost:8000/

