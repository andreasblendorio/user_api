import os
import dotenv

# Specificy a `.env` file containing key/value config values
dotenv_file = dotenv.find_dotenv(usecwd=True)
dotenv.load_dotenv(dotenv_file)

#basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir,'.env', '.flaskenv'))

'''
Creating this file avoids inline configs, which is BAD 
'''
# Creating a config class
class Config:

    # General-purpose config
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Database 
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MySQL bindings
    MYSQL_USER = 'root'
    MYSQL_HOST = 'localhost'
    MYSQL_PASSWORD = 'kernel23'
    MYSQL_DB = 'user_db'

    # For further development purpose
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
    # Testing
    TESTING = True
    SQLALCHEMY_ECHO = False