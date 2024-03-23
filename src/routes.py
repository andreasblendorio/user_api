from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from src.models import User, UserSchema, validate_custom_email, validate_user_status
from src import db, response_with, resp

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

# Defining a blueprint obj
user_bp = Blueprint('user_bp', __name__)

# Init schema
user_schema = UserSchema()

# Routing
'''
@app.route or @app.get,
no diffs given that the default for .route is method=['GET']
.get is just a shortcut for the same thing. 
BTW @app.get is more intent-revealing.
'''
# Indexing
@user_bp.get("/")
def index():
    return "Hello, World!"

# Welcoming fn
@user_bp.get("/hello")
def hello(): 
    return {"message": "Hello, World"}
    '''
    return jsonify({"message":"Hello, World!"}) 
    BTW this serialization it's a plus, 
    by default py dictionary is directly mapped to a json obj
    so it's fair to go with: return {"message":"Hello, World"}
    '''
# Routes for CRUD operations on db tables

# Retrieving a list of all the users
@user_bp.route('/users', methods=['GET'])
def get_users():
    fetched_users = User.query.all()
    serialized_users = user_schema.dump(fetched_users, many=True)  # Serialize all users
    return jsonify(serialized_users) #TODO: fix the return to be done with the response module
    

# Retrieving a single user record by providing the id
@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    serialized_user = user_schema.dump(user)
    return response_with(resp.SUCCESS_200, value=serialized_user)
  
# Creating a new user 
@user_bp.route('/user', methods = ['POST'])
def create_user():
    data = request.get_json() 
    new_user = User(**data)
    new_user.create()
    return response_with(resp.SUCCESS_201)
    
# Updating a user
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return response_with(resp.SUCCESS_204)

# Deleting a user
@user_bp.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    User.delete(user)
    return response_with(resp.SUCCESS_200)
   
# Update based on status field 
@user_bp.route('/users/<int:user_id>/<string:user_status>', methods=['PUT'])
def update_user_status(user_id):
    data = request.get_json()
    new_status = data.get('user_status') 

    try:
        validate_user_status(new_status)
    except ValidationError as e:
        return jsonify({"message": str(e)}), 400 #TODO: fix the return to be done with the response module

    user = User.query.get_or_404(user_id)
    user.user_status = new_status
    db.session.commit()
    return jsonify({"message": f"User status updated to {new_status} successfully"}) #TODO: fix the return to be done with the response module





















# Activating a user
@user_bp.route('/users/<int:user_id>/activate', methods=['PUT'])
def activate_user(user_id):
    user = User.query.get_or_404(user_id)
    if (User.user_status ==False):
        User.user_status == True
        db.session.commit(user)
        return jsonify({"message": "User activated successfully"})
    else:
        return jsonify({"message": "User status is already active"})

# Deactivating a user
@user_bp.route('/users/<int:user_id>/deactivate', methods=['PUT'])
def deactivate_user(user_id):
    user = User.query.get_or_404(user_id)
    User.user_status == False
    db.session.commit(user)
    return jsonify({"message": "User deactivated successfully"})