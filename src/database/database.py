from flask_pymongo import PyMongo

class Database:
    def __init__(self, app):
        app.config["MONGO_URI"] = "mongodb://localhost:27017/python_news"  # Cambia 'your_database_name' por el nombre de tu base de datos
        self.mongo = PyMongo(app)

    def get_db(self):
        return self.mongo.db