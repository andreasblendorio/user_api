# *user_api*

A simple RESTful API with Python, Flask & MySQL.

> [!IMPORTANT]
> This development project is mostly for learning purpose, indeed code readability might not be at its finest, so get rid of the multiline comments.

## Overview :mag_right:

This draft is a simple RESTful API built using Python Flask and SQLAlchemy to interact with a MySQL database. As such, the API provides basic CRUD (Create, Read, Update, Delete) operations to manage user data stored in the database.

> [!NOTE]
> It also includes Swagger documentation using OpenAPI to facilitate understanding and testing of the API endpoints.

## Requirements :pushpin:

- Python 3.x
- Flask
- MySQL RDBMS
- Swagger UI (optional, for documentation)

for further and more precise requirements you can refer to the [`requirements.txt`](/user_api/requirements.txt) file provided in this folder.

## Installation :inbox_tray:

### 1. Clone the repo

```git
git clone https://github.com/andreasblendorio/user_api.git
```

### 2. Install dependencies

```python
pip install -r requirements.txt
```

### 3. Configure MySQL Database

- Create a MySQL database via MySQL CLI, the one this API refers to is called *user_db*.

```mysql
mysql> CREATE DATABASE user_db;
```

the db table in this project will follow this structure:

```mysql
+----------------+
|      user      |
+----------------+
| user_id        |
| first_name     |
| last_name      |
| username       |
| user_password  |
| email          |
| telephone      |
| insertion_date |
| update_date    |
| user_status    |
+----------------+
```

- Update the database configuration in [`config.py`](/user_api/src/config/config.py) with your db credentials and configuation parameters.

> [!TIP]
> It is a good practice to have settings related to configurations saved in proper environment variables and manage these using `.env` or `.flaskenv` files.
>
> This project jas been developed using both `.env` and `.flaskenv` files, but you can't check them because they are gitignore(d).

So if you're planning to `git-clone` this repo make sure to create your own personal `.env` and `.flaskenv` files settled up like this:
```text
# .env
SECRET_KEY=your_secret_key
```

```text
# .flaskenv
FLASK_APP=name_of_the_app_you_want_to_serve
FLASK_ENV=your_env
FLASK_DEBUG=True
SQLALCHEMY_DATABASE_URI=mysql://root:password@host/your_db_name  
SQLALCHEMY_TRACK_MODIFICATIONS=False 
```

### 4. Run the Flask application

```pyhton
python run.py
```

or use the integrated vscode terminal, and start the **flask server** from there

```cmd
C:\path\to\your\workingdir> flask run
```

## Structure :open_file_folder:

Project files are structured as follows:

```text
└── user_api
    ├── src                          // API core handlers
    │   ├── config           
    │   │   └── config.py            // Configuration
    │   ├── static  
    │   │   └── openapi.yaml         // Swagger Documentation
    │   ├── tests
    │   │   └── test_user_api.py     // Tests 
    │   ├── utils
    │   │   ├── HTTP_status_code.py  // Status codes    
    │   │   └── responses.py         // Common response functions
    │   │  
    │   ├── __init__.py              // App factory
    │   ├── auth.py
    │   ├── models.py                // DB Models
    │   ├── routes.py                // Endpoint routes
    │   └── run.py                   // App runner
    │  
    ├── .gitignore        
    ├── README.md
    └── requirements.txt
```

## API Endpoints :dart:

Here are the endpoints exposed by the API to perform CRUD ops on the user table

- `GET /users`: Get all users
- `GET /users/{id}`: Get user by ID
- `POST /user`: Create a new user
- `PUT /users/{id}`: Update user by ID
- `DELETE /users/{id}/`: Delete user by ID
- `PUT /users/{id}/{user_status}`: Update user by ID

## Request and Response format :handshake:

When interacting with the [`user_api`](/user_api/) API, all data is exchanged in JSON format adhering to the standards outlined in the [Google JSON Style Guide](https://google.github.io/styleguide/jsoncstyleguide.xml).\
 The following is the expected format for requests and responses when performing CRUD operations on a user:

```json
{
    "user_id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "user_password": "ThisIsAStrongPassword123!password123",
    "email": "john.doe@example.com",
    "telephone": "1234567890",
    "insertion_date": "2024-03-21T12:00:00", 
    "update_date": "2024-03-21T12:00:00", 
    "user_status": "true" 
}

```

## Swagger Documentation :page_facing_up:

- Swagger documentation (will be) available at `/swagger` endpoint  
- Swagger UI can still be accessed via vscode's OpenAPI extension to view API documentation and test endpoints interactively.

## ToDos :paperclip:

Moving forward the codebase will be enhanced with more robust test scripts and improvements in security measures. So what will be addressed in the future is:

- **Testing Suite**: Strengthening our testing suite [`test_user_api.py`](src/tests/test_user_api.py) is paramount to ensuring the reliability and stability of our application. This involves not only increasing test coverage but also refining existing tests and introducing new ones to capture edge cases and potential vulnerabilities.
- **Vulnerability Management**: Implementing robust security measures to identifying and addressing vulnerabilities by establish protocols for identifying, prioritizing, and remedying security issues promptly. This includes handling critical vulnerabilities related to SQL injection, XSS, and other security concerns with utmost urgency.

## Contributing

Contributions & advices are welcome!\
Feel free to submit issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the **MIT License**. See the [LICENSE](https://mit-license.org/) file for details.
