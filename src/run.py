from src import create_app

# Init
app = create_app()

# driver fn
if __name__ == "__main__":
    app.run()



















'''
driver fn
Checking if the .py file is executed
directly (not imported as a module in another file). 
debug mode is on to prevent stopping the server when changes occurs in the code base

Rather than setting a .flaskenv file to re-run the application without specifying the FLASK_APP
FLASK_ENV environment variables, we can do it in code by means of the .run() 
method of the Flask Class imported above

good for common case, no good when in development mode
BTW still a valid method for invoking a non-automatic reloading application
''' 
#if __name__ == '__main__': 
    #create_app.run(debug=True)
