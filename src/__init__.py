from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow

from src.utils.responses import response_with
from src.utils import responses as resp
import logging

import os

'''
__init__.py serves double duty: it will contain the application factory,
and it tells Python that the user_api (flaskr by convention) directory
should be treated as a package.
'''

# Init db as an instance of SQLAlchemy class, making it globally accessible
db = SQLAlchemy()

# Init MySQL 
my_sql = MySQL()

# Init Marshmallow 
ma = Marshmallow()

# creating a Flask instance inside an "application factory" fn rather than globally
def create_app(test_config=None):
    '''
    WSGI as an istance of the Flask class imported above 
    name is the name of the current module (the .py file this code resides in)
    '''
    # create & config the app
    app = Flask(__name__, instance_relative_config=True)

    # not sure if load_dotenv() should be placed here or in config.py
    #load_dotenv()

    if test_config is None:
        app.config.from_mapping(
            # ENV
            SECRET_KEY = os.getenv("SECRET_KEY"),
            # SQLALCHEMY
            SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS = False,
            )
    else: 
        app.config.from_pyfile('config.py', silent=True)
    

    # checking if the instance folder (user_api) already exists, if not then makedirs
    # TODO: make it conditional, if dir doesn't exist : create it, else try/except
    #try:
        #os.makedirs(app.instance_path)
    #except OSError:
        #pass
    
    @app.after_request
    def add_header(response):
        return response
    
    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)
    
    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)
    
    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)
        
    from src import models

    # Init plugins
    db.init_app(app)
    my_sql.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from src.models import User
        db.create_all()
                           
        # Registering the blueprints for the routes endpoints (and eventually the auth) 
        from src.routes import user_bp

        app.register_blueprint(user_bp)
        #app.register_blueprint(auth)

        return app
    

    
 
    
   








