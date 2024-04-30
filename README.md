### Final code for the project *learning_log* of Chapters 18-20 from the book: _PYTHON CRASH COURSE 3<sup>rd</sup> EDITION: A Hands-On, Project-Based Introduction to Programming_ by _Eric Matthes_    
Link to the [book repo](https://github.com/Shreehar-KE/book-python-crash-course/)
<br/>

Screenshot:
![Homepage](./demo/screenshots/Homepage.png)
<br/>

Note: 
- This code is for local use only and has no configurations for a cloud deployment.
- This has few additional features(refer below) which are not mentioned in the book.   

<br/>

Additional Features
- Removed help text in the __Registration__ page.
- Restriction of __register__, __login__ & __logout__ pages as per the user's authentication.
  - This is to prevent a scenario like: Logged-in user trying the access the __register__ or __login__ url.
  - This is implemented using custom middleware in the `accounts` app.
- New `edit-blog` feature to edit a blog's title & visibility.
- Conditional Display of `create-post`, `edit-post` & `edit-blog` links in __blog__ page based on the user's authentication.
- __Recent Posts__ section in the Home page.  
  
<br/>

How to run this project:
1. Create a new virtual environment with the packages mentioned in [requirements.txt](requirements.txt) and activate it.
2. Run `python manage.py migrate` to create a new `db.sqlite3`.
3. Run `python manage.py createsuperuser` to create a new admin user.
   1. Enter username, email & password(won't be displayed)
4. Run `python manage.py runserver` to run the project.
5. Visit the url shown in the terminal
   1. For Ex. `https://127.0.0.1:8000/`
6. To access the admin dashboard, visit the `/admin` subpage.
   1. For Ex. `https://127.0.0.1:8000/admin`

<br/>

Learning Outcomes:
- Basic MVT architecture of Django
- Function based Views
- Forms in Django
- Basic Auth Functionality using Django
- Template Inheritance in Django
- Applying Bootstrap5 styling in Django
- Custom Middlewares in Django

<br/>

- Languages used : python3, html
- Frameworks used : django
- Libraries used : django-bootstrap5
- Tech Domain : Full-Stack-Development
