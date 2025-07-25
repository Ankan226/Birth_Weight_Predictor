from flask import Blueprint

#3 creating a blueprint/mini flask app for user object
user_bp = Blueprint("user", __name__)


@user_bp.route('/get-user', methods=['GET'])
def get_user():
    return "This is Get user route."

@user_bp.route('/update-user', methods=['PUT'])
def update_user():
    return "This is Update user route." 

@user_bp.route('/create-user', methods=['POST'])
def create_user():
    return "This is Create user route."

@user_bp.route('/delete-user', methods=['DELETE'])
def delete_user():
    return "This is Delete user route."