import json
import os

class Admin:
    ADMIN_FILE = os.path.join('dados', 'usuarios.json')

    @staticmethod
    def load_users():
        """Carrega a lista de usuários do arquivo JSON."""
        if not os.path.exists(Admin.ADMIN_FILE):
            return []
        with open(Admin.ADMIN_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def authenticate_admin(email, password):
        """Autentica um administrador verificando email e senha."""
        users = Admin.load_users()
        for user in users:
            if user["email"] == email and user["password"] == password and user["user_type"] == "Admin":
                return user
        return None

    @staticmethod
    def add_admin(name, email, password):
        """Adiciona um novo administrador ao sistema."""
        users = Admin.load_users()
        
        if any(user["email"] == email for user in users):
            raise ValueError("Este email já está cadastrado como administrador.")

        new_admin = {
            "name": name,
            "email": email,
            "password": password,
            "user_type": "Admin"
        }
        users.append(new_admin)

        with open(Admin.ADMIN_FILE, 'w', encoding='utf-8') as file:
            json.dump(users, file, indent=4)
        
        return "Administrador cadastrado com sucesso!"

    @staticmethod
    def list_admins():
        """Lista todos os administradores cadastrados."""
        users = Admin.load_users()
        return [user for user in users if user["user_type"] == "Admin"]
