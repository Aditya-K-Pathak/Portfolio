from django.shortcuts import render, HttpResponse
from . forms import userform
import json
import hashlib

def hash_password(password: str) -> str:
    """
    Hashes a password using SHA-256 algorithm.

    This function takes a plaintext password as input, encodes it in UTF-8,
    and then applies the SHA-256 hashing algorithm to produce a hexadecimal
    representation of the hash.

    Parameters:
    - password (str): The plaintext password to be hashed.

    Returns:
    - str: The hexadecimal digest of the hashed password.
    """
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()

class UserFunction:

    @staticmethod
    def read_file() -> dict:
        """
        Reads and returns the content of the users.json file as a dictionary.

        This method opens the 'sites/users.json' file in read mode, loads its JSON content using the json module,
        and returns the content as a dictionary. This is used to retrieve the current state of users stored in the file.

        Returns:
            dict: A dictionary containing the users data loaded from the JSON file.
        """
        with open('sites/users.json', 'r') as file:
            return json.load(file)
        
    @staticmethod
    def write_file(users: dict):
        """
        Writes the given users dictionary to the 'sites/users.json' file.

        This method takes a dictionary of users, converts it into JSON format, and writes it to the 'sites/users.json' file.
        It uses an indentation of 4 spaces for better readability of the JSON file.

        Parameters:
        - users (dict): A dictionary containing the users data to be written to the file.

        Returns:
        - None
        """
        with open('sites/users.json', 'w') as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def validate_user(username: str, password: str) -> str:
        """
        Validates a user's login credentials.

        This method checks if the provided username exists in the users.json file. If the username exists,
        it then verifies whether the provided password matches the hashed password stored for that user.
        It returns a message indicating whether the user was found, the password was incorrect, or if it's a new user.

        Parameters:
        - username (str): The username of the user attempting to log in.
        - password (str): The plaintext password provided by the user for login.

        Returns:
        - str: A message indicating the result of the validation. Possible values are "User Found", "Incorrect Password",
            or "New User" if the username does not exist in the database.
        """
        users = UserFunction.read_file()
        if username in users:
            if users[username]['password'] == hash_password(password):
                return "User Found"
            else:
                return "Incorrect Password"
        return "New User"
    
    @staticmethod
    def add_user(username: str, password: str, email: str) -> str:
        """
        Adds a new user to the users.json file.

        This method takes a username, password, and email as input. It hashes the password using the hash_password function,
        then creates a new entry in the users dictionary with the username as the key and a dictionary containing the hashed
        password and email as the value. This updated users dictionary is then written back to the users.json file.

        Parameters:
        - username (str): The username of the new user.
        - password (str): The plaintext password of the new user.
        - email (str): The email address of the new user.

        Returns:
        - str: Returns True indicating the user was successfully added.
        """
        users = UserFunction.read_file()
        users[username] = {
            'password': hash_password(password),
            'E-mail': email
        }
        UserFunction.write_file(users)
        return True
    
    @staticmethod
    def is_url_present(username: str, url: str) -> bool:
        """
        Checks if a given URL is already associated with a user.

        This method reads the current users data from the 'sites/users.json' file and checks if the specified URL
        is already present under the given username's data. It is used to prevent duplicate URLs for the same user.

        Parameters:
        - username (str): The username of the user to check the URL for.
        - url (str): The URL to be checked for presence under the user's data.

        Returns:
        - bool: True if the URL is already present under the user's data, False otherwise.
        """
        users =  UserFunction.read_file()
        if url in users[username]:
            return True
        return False

    @staticmethod
    def add_url(username: str, url: str, html: str) -> bool:
        """
        Adds a new URL and its corresponding HTML content to a user's data.

        This method updates the users.json file by adding a new URL and its associated HTML content under the specified user's data.
        It ensures that each user can store multiple URLs along with their HTML content. After updating the user's data, it writes
        the updated data back to the users.json file.

        Parameters:
        - username (str): The username of the user to whom the URL will be added.
        - url (str): The URL to be added.
        - html (str): The HTML content associated with the URL.

        Returns:
        - bool: True indicating that the URL and HTML content were successfully added to the user's data.
        """
        users = UserFunction.read_file()
        users[username][url] = html
        UserFunction.write_file(users)
        return True

def get_template(url: str, html: str) -> str:
    """
    Generates a Django view function template as a string.

    This function creates a template for a Django view function. The template includes a function definition
    that takes a request object as a parameter and returns an HttpResponse object with the specified HTML content.
    The name of the function is dynamically set based on the provided URL parameter.

    Parameters:
    - url (str): The URL that will be used as the name of the view function.
    - html (str): The HTML content to be returned by the view function.

    Returns:
    - str: A string representation of the Django view function template.
    """
    return f"""def {url}(request):\n\treturn HttpResponse('{html}')"""

def addtoviews(url: str, html: str) -> None:
    """
    Appends a new Django view function to the 'sites/views.py' file.

    This function generates a Django view function template using the provided URL and HTML content. It then opens the
    'sites/views.py' file in append mode and adds the generated view function to the end of the file. This allows dynamically
    adding new view functions to handle requests for new URLs.

    Parameters:
    - url (str): The URL that will be used as the name of the view function. This should be a valid Python function name.
    - html (str): The HTML content to be returned by the view function. This content will be directly included in the generated
      view function, so it should be properly escaped to avoid syntax errors.

    Returns:
    - None
    """
    with open('sites/views.py', 'a+') as file:
        file.write('\n' + get_template(url, html))
        file.close()

def addtourls(url: str, html: str) -> None:
    """
    Adds a new URL pattern to the Django project's URL configuration.

    This function reads the existing URL patterns from 'sites/urls.py', inserts a new URL pattern that maps
    the given URL to a view function with the same name as the URL, and then writes the updated list of URL patterns
    back to 'sites/urls.py'. This allows dynamically adding new URL routes to the Django project.

    Parameters:
    - url (str): The URL to be added to the URL configuration. This should be a valid URL pattern string.
    - html (str): This parameter is not used in the function but is included to match the function signature.
                  It can be ignored or removed if not necessary.

    Returns:
    - None
    """
    with open('sites/urls.py', 'r') as file:
        urlpattern = file.readlines()
        # Insert the new URL pattern before the last line (assumed to be a closing bracket or similar)
        urlpattern.insert(-1, f""" path('{url}', views.{url}),\n""")
        with open('sites/urls.py', 'w') as file:
            file.writelines(urlpattern)
    

# Create your views here.
def index(request):
    """
    Handles the index view of the site, processing both GET and POST requests.

    For GET requests, it renders the site's index page with a user form.
    For POST requests, it processes the submitted form data to either add a new URL to an existing user,
    add a new user along with their URL, or return an error message if the username or password is incorrect.

    Parameters:
    - request: HttpRequest object containing metadata about the request.

    Returns:
    - HttpResponse: For POST requests, returns an HttpResponse indicating the outcome of the operation (URL added, URL already in use, or incorrect username/password).
                    For GET requests, renders the index page with the user form.
    """
    if request.method == 'POST':
        # Extract form data from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        url = request.POST.get('url')
        html = request.POST.get('html')
        
        # Validate user credentials
        if UserFunction.validate_user(username, password) == "User Found":
            # Check if the URL is already associated with the user
            if not UserFunction.is_url_present(username, url):
                # Add the new URL and its HTML content to the user's data
                UserFunction.add_url(username, url, html)
                # Dynamically add a new view and URL pattern for the added URL
                addtoviews(request.POST.get('url'), request.POST.get('html'))
                addtourls(request.POST.get('url'), request.POST.get('html'))
                return HttpResponse(f'URL Added...')
            else:
                return HttpResponse('URL already in use')
        elif UserFunction.validate_user(username, password) == "New User":
            # Add a new user and their URL to the system
            UserFunction.add_user(username, password, email)
            UserFunction.add_url(username, url, html)
            # Dynamically add a new view and URL pattern for the added URL
            addtoviews(request.POST.get('url'), request.POST.get('html'))
            addtourls(request.POST.get('url'), request.POST.get('html'))
            return HttpResponse('URL Added...')
        else:
            return HttpResponse('Incorrect Username or Password')
        
    # For GET requests, render the index page with the user form
    return render(request, 'sitesindex.html', {'form': userform})

# User's view
