# Client and Project Management System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Database Configuration](#database-configuration)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Admin Panel Usage](#admin-panel-usage)

## Project Overview
This project is a web-based **Client and Project Management System** built using Django and Django REST Framework. It allows users to manage clients and projects in a multi-user environment. Admin users can create clients and assign projects to them, while also assigning users to those projects. The project provides APIs to fetch clients, update them, and handle their associated projects.

## Features
- Register new clients
- Update or delete client information
- Create and assign projects to clients
- Assign multiple users to projects
- List all clients and their associated projects
- Retrieve all projects assigned to the currently logged-in user
- Django admin interface for managing users, clients, and projects

## Technologies Used
- **Django** - Web framework for building the backend
- **Django REST Framework (DRF)** - For building RESTful APIs
- **MySQL** - Relational database for data storage
- **Python 3.x** - Programming language
- **HTML/CSS** - Django admin styling

## Setup Instructions
Follow these steps to set up and run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/jyotik03/Django_Python_Machine_Test
   cd Django_Python_Machine_Test

2. Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3. Install the dependencies:
pip install -r requirements.txt

4. Set up the database:

- Install MySQL if not already installed.
- Create a MySQL database (e.g., client_project_db).
- Update DATABASES configuration in settings.py as shown in the Database Configuration section.
5. Apply migrations:

python manage.py migrate

6. Create a superuser:
python manage.py createsuperuser

7. Run the development server:
python manage.py runserver

8. Access the admin panel at http://127.0.0.1:8000/admin/ and login with your superuser credentials.

## Database Configuration
In settings.py, update the DATABASES section to use MySQL:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'client_project_db',  # Replace with your database name
        'USER': 'root',  # Replace with your MySQL username
        'PASSWORD': 'password',  # Replace with your MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
## API Endpoints
### Clients API
- List all clients: GET /clients/
- Create a new client: POST /clients/
- Retrieve client details with projects: GET /clients/:id/
- Update a client: PUT-PATCH /clients/:id/
- Delete a client: DELETE /clients/:id/
### Projects API
- Create a new project for a client: POST /clients/:id/projects/
- Retrieve projects assigned to the logged-in user: GET /projects/
### Usage
- #### Create and Manage Clients:
1. To create a client, use the POST /clients/ endpoint with the following input:

{
    "client_name": "Example Client"
}
2. To retrieve details of a specific client and its projects, use GET /clients/:id/.

#### Assign Projects to Users:
After creating a client, you can assign a project to that client using the POST /clients/:id/projects/ endpoint, specifying the project_name and the list of users (by their IDs):

{
    "project_name": "New Project",
    "users": [
        {
            "id": 1,
            "name": "User One"
        }
    ]
}
#### Retrieve Projects of Logged-In User:
Use the GET /projects/ endpoint to list all projects assigned to the currently logged-in user.
#### Admin Panel Usage
1. Go to the Django Admin interface at http://127.0.0.1:8000/admin/.
2. Log in using your admin credentials.
3. From here, you can manage:
- Clients: Add, update, and delete clients.
- Projects: Add projects for clients and assign users to them.
- Users: Manage the registered users in the system.
#### Assign Projects to Users in Admin Panel:
1. Go to the Projects section in the admin panel.
2. Add or edit a project, and select the client to which the project belongs.
3. Use the Users field to assign users to the project.
