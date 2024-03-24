# *user_api*

A simple RESTful API with Python, Flask & SQLAlchemy.

## Overview

This draft is a simple RESTful API built using Python Flask and SQLAlchemy to interact with a MySQL database. As such, the API provides basic CRUD (Create, Read, Update, Delete) operations to manage user data stored in the database. It also includes Swagger documentation using OpenAPI to facilitate understanding and testing of the API endpoints.

## Requirements

- Python 3.x
- Flask
- SQLAlchemy
- MySQL rdbms
- Swagger UI (optional, for documentation)

for further more precise requirements you can refer to the requirements.txt file provided in this folder.

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

- Create a MySQL database, the one this API refers to is called *user_db*.
- Update the database configuration in *config.py* with your db credentials.and configuation parameters.

### 4. Run the Flask application

```bash
python run.py
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

## Request and Response format

## Swagger Documentation

- Swagger documentation (will be) available at `/swagger` endpoint  
- Access the Swagger UI via vscode OpenAPI extension to view API documentation and test endpoints interactively.

## ToDos

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.