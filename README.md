
# Travel App

The Django Travel App Backend is designed to serve as the backend system for a travel app that manages travel destinations. It provides a RESTful API for performing CRUD operations on destinations, includes authentication functionality, and implements basic error handling to ensure smooth operation.


## Steps to Run this Project

Step 1: Clone the project https://github.com/truptighadge/Travel-App

Step 2: cd ~/travel_app

Step 3: Create Virtualenv (Python 3) virtualenv -p python3 travel_appenv

Step 4: Activate Virtualenv source travel_appenv/bin/activate

Step 5: Install Dependencies pip install -r requirements.txt

Step 6: Migrate To Database python manage.py migrate

Step 7: Create Admin python manage.py createsuperuser # Give Username and Password of Your Choice

Step 8: Run the Project python manage.py runserver # This will run the project on 127.0.0.1:8000

Step 9: Open URL http://127.0.0.1:8000 in the browser

Step 10: http://127.0.0.1:8000/admin/  to access admin panel. ( Provide Username and Password you used while creating admin) and entries using the admin panel
## API Reference

## Authentication
   ### Registration
    Endpoint: POST /accounts/register/
    Description: Register a new user.

   ### Login
    Endpoint: POST /accounts/api-token-auth/
    Description: Obtain an authentication token by  providing valid credentials.

   ### Logout
    Endpoint: GET /accounts/logout/
    Description: Logs out the current user and invalidates the authentication token.

## Destinations

### Retrieve all destinations
    Endpoint: GET /destinations/
    Description: Get a list of all destinations.

### Create a destination
    Endpoint: POST /destinations/
    Description: Create a new destination.

### Retrieve a destination record
    Endpoint: GET /destinations/<int:pk>/
    Description: Get details of a specific destination identified by its primary key.
   
### Update a destination record
    Endpoint: PUT /destinations/<int:pk>/
    Description: Update details of a specific destination identified by its primary key.  

### Delete a destination record
    Endpoint: DELETE /destinations/<int:pk>/
    Description: Delete a specific destination identified by its primary key.















