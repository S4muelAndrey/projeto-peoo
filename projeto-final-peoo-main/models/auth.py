import json
import os

class Auth:
    USER_FILE = os.path.join('dados', 'usuarios.json')

    @staticmethod
    def load_users():
        if not os.path.exists(Auth.USER_FILE):
            return []
        with open(Auth.USER_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def save_users(users):
        with open(Auth.USER_FILE, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def authenticate(email, password):
        users = Auth.load_users()
        for user in users:
            if user['email'] == email and user['password'] == password:
                return user
        return None

    @staticmethod
    def register(name, email, password, user_type):
        users = Auth.load_users()
        if any(user['email'] == email for user in users):
            raise ValueError('Este email já está cadastrado.')
        new_user = {
            'name': name,
            'email': email,
            'password': password,
            'user_type': user_type
        }
        users.append(new_user)
        Auth.save_users(users)
        return 'Cadastro realizado com sucesso!'
