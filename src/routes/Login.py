from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.User import User
# Models
from models.ModelUser import ModelUser

main = Blueprint('movie_blueprint', __name__)


@main.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['usuario']
        password = (request.json['contrasena'])
        user = User("", username, password, "", "")

        logged_user = ModelUser.login(user)

        print(logged_user)

        if logged_user != None:
            if logged_user.password == password:
                new_token = None

                if User.verify_expiration(logged_user.date):
                    new_token = str(uuid.uuid4())

                    affected_rows = ModelUser.update_token(logged_user.id, new_token)

                    if affected_rows != 1:
                        return jsonify({
                            "estado": False,
                            "descripcionRespuesta": "Error inesperado",
                        }), 500

                return jsonify({
                    "estado": "true",
                    "descripcionRespuesta": "",
                    "token": new_token or logged_user.token
                })
            else:
                return jsonify({
                    "estado": False,
                    "descripcionRespuesta": "Usuario o contraseña incorrecto",
                }), 500
        else:
            return jsonify({
                    "estado": False,
                    "descripcionRespuesta": "Usuario no encontrado",
                }), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500