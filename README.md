# Social Network Web Application

## Technologies Used
- **Python**: Core programming language.
- **Flask**: Micro web framework for Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Google OAuth 2.0**: Authentication mechanism.
- **Flask-Dance**: Flask extension for OAuth authentication.
- **pipenv**: Dependency management tool.
- **git**: Version control system.

## Screens
1. **Landing Page (`/`)**: Introduction and overview of the application.
   - Route: `landing_page`

2. **OAuth (`/oauth`)**: Authentication and authorization using Google OAuth.
   - Route: `oauth`

3. **Sign In (`/signin`)**: User login page.
   - Route: `sign_in`

4. **Sign Up (`/signup`)**: User registration page.
   - Route: `sign_up`

5. **Update Profile (`/profile`)**: Page to update user information.
   - Route: `update_profile`

6. **API (`/api`)**: Endpoint for API interactions.
   - Route: `api`

7. **Create Post (`/create/post`)**: Form to create new posts.
   - Route: `create_post`

8. **Logged In - View Posts (`/loggedin`)**: View posts after logging in.
   - Route: `logged_in`

## Key Ideas
- **MVC Design Pattern**: Separation of concerns into Model (data), View (presentation), and Controller (logic).
- **Scalable Application Design**: Organized structure to handle growth and maintainability.
- **OAuth Integration**: Secure authentication mechanism using Google OAuth.
- **Flask and SQLAlchemy**: Utilizing Flask for web development and SQLAlchemy for database interactions.

## Design and Architecture
The application is structured around the MVC pattern, emphasizing separation of concerns:
```
.
├── config
│ └── settings.py # Configuration settings
└── socialnetwork
├── utils
├── models # Database models (M)
├── routes # Controllers (C)
├── templates # Views (V)
├── forms # Form handling
└── static # Static assets (images, CSS)
```

- **Config**: Configuration settings for the application.
- **socialnetwork**: Main application directory.
  - **utils**: Utility functions.
  - **models**: Database models (representing entities like users and posts).
  - **routes**: Controllers handling HTTP requests and responses.
  - **templates**: HTML templates rendered by Flask.
  - **forms**: Forms for user input handling.
  - **static**: Static files such as images and CSS styles.

## API
- **Endpoint**: `{URI}/api/v1/posts/json`
- **Description**: Provides JSON data for posts.

## Installation
### Requirements
- Python 3.5+
- `requirements.txt` file listing necessary packages.

### How to Run the Project
1. Download the project to your computer.
2. Navigate to the project directory (`src/web`).
3. Set up a virtual environment (`virtualenv ENV`).
4. Activate the virtual environment (`source env/scripts/activate` on Windows, or `source env/bin/activate` on macOS/Linux).
5. Install dependencies using `pip` (`pip install -r requirements.txt`).
6. Set the Flask application entry point (`export FLASK_APP=manage.py`).
7. Run the application (`flask run`).
8. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

