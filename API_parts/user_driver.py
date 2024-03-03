from flask import request, Blueprint
from hasher import hasher
from DB_wrappers.models import Users
from app import app, db
from helpers.user_helper import verify_profile_permission, verify_email

auth = Blueprint('auth', __name__, template_folder='API_parts')


@auth.route('/auth')
@auth.get("/user")
def get_user():
    if request.args.get('id'):
        user = Users.query.filter_by(id=request.args.get('id')).first()
        return user.email


@auth.post("/user/all")
def get_user_info():
    if not request.is_json:
        return {"error": "Request must be JSON"}, 415
    
    user = request.get_json()
    if not user.get('email') or not user.get('password'):
        return {"error": "Missing required fields"}, 406
    if not verify_email(user.get('email')):
        return {"error": "Uncorrectly formatted email"}
    if not verify_profile_permission(user.get('email'), hasher(user.get('password'))):
        return {"error": "Wrong email or password"}

    with app.app_context():
        user = Users.query.filter_by(
            email=user.get('email'),
            hashed_pwd=hasher(user.get('password'))) \
            .first()
    return user.to_dict()


@auth.post("/register")
def add_user():
    if not request.is_json:
        return {"error": "Request must be JSON"}, 415

    user = request.get_json()
    if not user.get('password') or not user.get('email'):
        return {"error": "Missing required fields"}, 406
    hashed = hasher(user.get('password'))

    with app.app_context():
        new_user = Users(hashed_pwd=hashed, email=user.get('email'))
        db.session.add(new_user)
        db.session.commit()

    return user, 201
