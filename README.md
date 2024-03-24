# *user_api*

A simple RESTful API with Python, Flask & SQLAlchemy.

## Overview

This draft is a simple RESTful API built using Python Flask and SQLAlchemy to interact with a MySQL database. As such, the API provides basic CRUD (Create, Read, Update, Delete) operations to manage user data stored in the database. It also includes Swagger documentation using OpenAPI to facilitate understanding and testing of the API endpoints.

## Requirements

- Requirements
- Python 3.x
- Flask
- SQLAlchemy
- MySQL rdbms
- Swagger UI (optional, for documentation)

for further more precise requirements you can refer to the requirements.txt file provided in this folder.

## Installation

### 1. Clone the repo

### 2. Install dependencies

### 3. Configure MySQL Database

- Create a MySQL database, the one this API refers to is called *user_db*.
- Update the database configuration in *config.py* with your db credentials.and configuation parameters.
- Run the flask application.

## Structure
```
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
    │   └── run.py                   // App runnes
    ├── .flaskenv
│   ├── .gitignore        
    ├── README.md
    └── requirements.txt
```

## API Endpoints

## Request and Response format

## Swagger Documentation

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.