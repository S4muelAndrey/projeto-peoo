from models.auth import Auth

class AuthController:
    @staticmethod
    def login(email, password):
        user = Auth.authenticate(email, password)
        if user:
            return user
        else:
            raise ValueError('Email ou senha inválidos.')

    @staticmethod
    def register(name, email, password, user_type):
        return Auth.register(name, email, password, user_type)
