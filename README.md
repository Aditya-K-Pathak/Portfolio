# Portfolio
This Repository contains my portfolio built using Django.

The portfolio contains files like settings, urls, wsgi etc.
In order to host the project over internet a user need to so slight modification in the code by adding the name of the host link in settings.py.

Requirement: Django
Installation Command - pip install django

To run the code on localhost a user need to be in the folder where manage.py is situated. In the same directory execute the code below
python3 manage.py runserver

Composition - 
./static/ - contains image and css for the website i.e., static files.
./templates/ - contains html file for redirecting urls to specific webpage.

**Update Log**
#V.0.3.0
- Set Debug = False
- Removed Static File dependencies
- Added Page not Found Error Page
