# Import necessary modules and classes
from django.shortcuts import render, redirect
from .form import *
from . import actions
from . import mailverification
import json

# Define a constant for IP address and load data from JSON file
IP_ADDRESS = [None]

with open("static/data/data.json", "r") as file:
    data = json.loads(file.read())

# Function to handle newsletter subscription logic
def NewsLetter_(request: any):
    # Instantiate a NewsLetter form
    data['newsletter'] = NewsLetter()
    
    # Check if the request method is POST
    if request.method == "POST":
        # Check if the 'email' field is present in the POST data
        if request.POST.get('email'):
            # Call the subscribeToNewsLetter function from actions module
            actions.NewsLetter.subscribeToNewsLetter(
                request.POST.get('email')
            )

# Function to fetch weather data based on IP address
def Temperature(request: any):
    # Instantiate an Ip form
    data['weather'] = Ip()
    
    # Check if the request method is POST
    if request.method == "POST":
        # Check if the 'ip_address' field is present in the POST data
        if request.POST.get('ip_address'):
            # Update IP_ADDRESS with the provided IP address
            IP_ADDRESS[0] = request.POST.get('ip_address')
            # Fetch temperature data based on the IP address
            data['Temperature'] = actions.Coordinates.getCoordinates(
                IP_ADDRESS[0]
            )

# Function to handle common tasks and log temperature data
def interface(request: any, page: str):
    # Call NewsLetter_ and Temperature functions
    NewsLetter_(request)
    Temperature(request)
    
    # Check if temperature data is available in the 'data' dictionary
    if 'Temperature' in data:
        # Log temperature data for the current IP address and page
        actions.Logger().readLog(IP_ADDRESS[0], data['Temperature'][1], page)
    else:
        # Log an error for the current IP address and page
        actions.Logger().readLog(IP_ADDRESS[0], 'Error', page)

# View function to render the home page
def index(request):
    # Call the interface function for the home page
    interface(request, 'Home')
    # Render the index.html template with dynamic data
    return render(request, 'index.html', data)

# View function to render the patents page
def patents(request):
    # Call the interface function for the patents page
    interface(request, 'Patents')
    # Update 'data' dictionary with patents data
    data.update(data['Patents'])
    # Render the patents.html template with dynamic data
    return render(request, 'patents.html', data)

# View function to render the awards page
def awards(request):
    # Call the interface function for the awards page
    interface(request, 'Awards')
    # Render the awards.html template with dynamic data
    return render(request, 'awards.html', data)

# View function to render the projects page
def projects(request):
    # Call the interface function for the projects page
    interface(request, 'Projects')
    # Render the projects.html template with dynamic data
    return render(request, 'projects.html', data)

# View function to render the research page
def research(request):
    # Call the interface function for the research page
    interface(request, 'Research')
    # Render the research.html template with dynamic data
    return render(request, 'research.html', data)

# View function to render the Contact page
def contact(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Store Required Data
        if request.POST.get('Name'):
            Name = request.POST.get('Name')
            Email = request.POST.get('Email')
            Comment = request.POST.get('Comment')
            if mailverification.validationHandler.initiateValidation(
                Name, Email
            ):
                return redirect('./verification')
            actions.Contacts.addQuery(Name, Email, Comment)

    # Call the interface function for the Contact page
    interface(request, 'Contact')
    # Add an instance of contactForm form to data
    data.update({
        'ContactForm': ContactForm()
    })
    # Render the contact.html template with dynamic data
    return render(request, 'contact.html', data)

def verification(request):
    if request.method == 'POST':
        if request.POST.get('pin'):
            if mailverification.validationHandler.checkValidation(
                request.POST.get('Email'), request.POST.get('pin')
            ):return redirect('./contact')
    interface(request, 'Contact')
    return render(request, 'verificationpage.html', {'form': Verification()})