from flask import request, jsonify
from flask import current_app
from src.database.database import Database  
from bson.objectid import ObjectId  # Import ObjectId from bson

class UserController:
    def __init__(self):
        self.db = None

    def set_database(self):
        # Obtener la instancia de la base de datos desde la aplicación actual
        self.db = Database(current_app)

    def home(self):
        return "¡Hola, mundo! Estás en la página principal."

    def add_user(self):
        data = request.json
        name = data.get('name')
        role = data.get('role')
        email = data.get('email')

        # Ensure the database is set up
        if self.db is None:
            self.set_database()

        try:
            # Check if the user already exists
            existing_user = self.db.get_db().users.find_one({'email': email})
            if existing_user:
                return jsonify({'error': 'El usuario ya existe con este correo electrónico.'}), 400

            # Create a new user with a unique ID
            user_id = str(ObjectId())  # Generate a unique ID
            self.db.get_db().users.insert_one({'_id': user_id, 'name': name, 'role': role, 'email': email})

            return jsonify({'message': 'Usuario agregado exitosamente!', 'user_id': user_id}), 201

        except errors.PyMongoError as e:
            return jsonify({'error': 'Error al agregar el usuario: ' + str(e)}), 500
        
    def get_all_users(self):
        if self.db is None:
            self.set_database()

        try:
            users = list(self.db.get_db().users.find({}, {'_id': 0}))  # Excluye el campo _id
            return jsonify(users), 200
        except errors.PyMongoError as e:
            return jsonify({'error': 'Error al recuperar los usuarios: ' + str(e)}), 500
    
    def get_user_by_id(self, user_id):
        # Asegúrate de que la base de datos esté configurada
        if self.db is None:
            self.set_database()

        try:
            user = self.db.get_db().users.find_one({'_id': ObjectId(user_id)}, {'_id': 0})  # Excluye el campo _id
            if user:
                return jsonify(user), 200
            else:
                return jsonify({'error': 'Usuario no encontrado.'}), 404
        except errors.PyMongoError as e:
            return jsonify({'error': 'Error al recuperar el usuario: ' + str(e)}), 500
        except Exception as e:
            return jsonify({'error': 'Error en la solicitud: ' + str(e)}), 400