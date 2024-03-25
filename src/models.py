from src import db
from datetime import datetime
from marshmallow import Schema, fields, ValidationError
'''
For further validations of the fields the package IntegrityErros
may be suitable 
#from sqlalchemy.exc import IntegrityError
'''
# User class
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True) # maybe autoincrement = True
    first_name = db.Column(db.String(100), nullable=False) # nullable set to False 'cause we don't want this to be blank
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    user_password = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telephone = db.Column(db.String(200), nullable=False)
    insertion_date = db.Column(db.DateTime, default=datetime.now)
    update_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    user_status = db.Column(db.String(20), default=True)
    '''
    Apparently there's no need to init this class 'cause SQLAlchemy
    automatically defines an __init__ method
    for each model that assigns any keyword arguments to corresponding
    database columns and other attributes.
    '''
    def __init__(self, user_id, first_name, last_name, username, user_password, email, telephone, insertion_date, update_date, user_status):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username 
        self.user_password = user_password 
        self.email = email
        self. telephone = telephone 
        self.insertion_date = insertion_date 
        self.update_date = update_date
        self.user_status = user_status
    
    # Shortcur functions for db ops
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self):
        db.session.delete(self)
        db.session.commit
        return self
 
    # User class method .serialize 
    # NOTE: by using Marshmallow schemas, this fn may become redundant, BTW leaving it here just in case
    # converting an instance of a User obj in a pyhton dic containing the values of the attributes of the user 
    def serialize(self):
        return {
            'user_id' : self.user_id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'username' : self.username,
            'user_password' : self.user_password,
            'email': self.email,
            'telephone': self.telephone,
            'insertion_date': self.insertion_date,
            'update_date': self.update_date,
            'user_status': self.user_status
        }

    # Representing User obj as a string
    def __repr__(self):
        return '<User %r>' % self.username

# Possible user_status values
VALID_USER_STATUSES = {'active', 'inactive', 'pending', 'deleted', 'blocked'}

# Validation fn for user_status
def validate_user_status(value):
    if value not in VALID_USER_STATUSES:
        raise ValidationError(f"Invalid user status. Must be one of {', '.join(VALID_USER_STATUSES)}")

# Validation fn for email format
def validate_custom_email(value):
    if "@" not in value or "." not in value.split("@")[-1]:
        raise ValidationError("Invalid email format. Email must contain '@' and '.' in the domain part.")

# Defining a Schema to be used by marshmallow
class UserSchema(Schema):
    user_id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    user_password = fields.String(required=True)
    email = fields.Email(required=True, validate = validate_custom_email)
    telephone = fields.String(required=True)
    insertion_date = fields.DateTime()
    update_date = fields.DateTime()
    user_status = fields.String(required=True, default=True, validate = validate_user_status)
