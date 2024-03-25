# *user_api*

A simple RESTful API with Python, Flask & SQLAlchemy.

## Overview

This draft is a simple RESTful API built using Python Flask and SQLAlchemy to interact with a MySQL database. As such, the API provides basic CRUD (Create, Read, Update, Delete) operations to manage user data stored in the database.

> [!NOTE]
> It also includes Swagger documentation using OpenAPI to facilitate understanding and testing of the API endpoints.

## Requirements

- Python 3.x
- Flask
- MySQL RDBMS
- Swagger UI (optional, for documentation)

for further and more precise requirements you can refer to the requirements.txt file provided in this folder.

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/andreasblendorio/user_api.git
```

### 2. Install dependencies

```bash
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

- Update the database configuration in *config.py* with your db credentials and configuation parameters.

### 4. Run the Flask application

```bash
python run.py
```

or use the integrated vscode terminal, and start the **flask server** from there

```bash
C:\path\to\your\working_dir> flask run
```

## Structure

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
    │   ├── __init__.py              // App factory
    │   ├── auth.py
    │   ├── models.py                // DB Models
    │   ├── routes.py                // Endpoint routes
    │   └── run.py                   // App runner
    ├── .flaskenv
    ├── .gitignore        
    ├── README.md
    └── requirements.txt
```

## API Endpoints

Here are the endpoints exposed by the API to perform CRUD ops on the user table

- `GET /users`: Get all users
- `GET /users/{id}`: Get user by ID
- `POST /user`: Create a new user
- `PUT /users/{id}`: Update user by ID
- `DELETE /users/{id}/`: Delete user by ID
- `PUT /users/{id}/{user_status}`: Update user by ID

## Request and Response format

When interacting with the [`user_api`](/user_api/) API, all data is exchanged in JSON format adhering to the standards outlined in the [Google JSON Style Guide](https://google.github.io/styleguide/jsoncstyleguide.xml).\
 The following are the expected formats for requests and responses for CRUD operations on a user:

## Swagger Documentation

- Swagger documentation (will be) available at `/swagger` endpoint  
- Access the Swagger UI via vscode OpenAPI extension to view API documentation and test endpoints interactively.

## ToDos

Moving forward the codebase will be enhanced with more robust test scripts and improvements in security measures. So what will be addressed in the future is:

- **Testing Suite**: Strengthening our testing suite [`test_user_api.py`](src/tests/test_user_api.py) is paramount to ensuring the reliability and stability of our application. This involves not only increasing test coverage but also refining existing tests and introducing new ones to capture edge cases and potential vulnerabilities.
- **Vulnerability Management**: Implementing robust security measures to identifying and addressing vulnerabilities by establish protocols for identifying, prioritizing, and remedying security issues promptly. This includes handling critical vulnerabilities related to SQL injection, XSS, and other security concerns with utmost urgency.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.