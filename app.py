from flask import Flask
from src.routes.user.user import user_blueprint
from src.database.database import Database  # Asegúrate de que la importación sea correcta

# Crear una instancia de Flask
app = Flask(__name__)

# Inicializar la conexión a la base de datos
db = Database(app)

# Register the blueprint
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
