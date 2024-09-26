from flask import Blueprint
from src.controller.user_controller import UserController

# Crea un blueprint llamado 'user'
user_blueprint = Blueprint('user', __name__)
user_controller = UserController()  

@user_blueprint.route('/', methods=['GET'])
def home_route():
    return user_controller.home()

@user_blueprint.route('/add_user', methods=['POST'])
def add_user_route():
    return user_controller.add_user()

@user_blueprint.route('/users', methods=['GET'])  # Nueva ruta para obtener todos los usuarios
def get_all_users_route():
    return user_controller.get_all_users()

@user_blueprint.route('/user/<string:user_id>', methods=['GET'])  # Nueva ruta para obtener un usuario por ID
def get_user_by_id_route(user_id):
    return user_controller.get_user_by_id(user_id)
