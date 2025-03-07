from models.auth import Auth
class AuthController:
    @staticmethod
    def login(email, password):
        # Verifica se o login é do admin
        if email == "admin@adm.com" and password == "SenhaDoAdmin":
            return {"name": "Administrador", "email": email, "user_type": "Admin"}
        
        # Caso contrário, segue com a autenticação normal (ex: usando a classe Auth)
        user = Auth.authenticate(email, password)
        if user is None:
            raise ValueError("Email ou senha incorretos.")
        return user


    @staticmethod
    def register(name, email, password, user_type):
        return Auth.register(name, email, password, user_type)
