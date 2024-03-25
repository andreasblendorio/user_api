from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth/me") 
# TODO: check which url prefix is right for my project
# NOTE: after defining a Blueprint, it has to be registered on your app instance (__init__.py)

# Handling a signup request
@auth.post("/register")
def register():
    return "User created"

# Retrieving my instance
@auth.get("/me")
def me():
    return {"user":"me"}

