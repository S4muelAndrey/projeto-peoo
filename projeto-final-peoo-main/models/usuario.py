import re
from models.persistencia import Persistencia

class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, novo_id):
        if isinstance(novo_id, int):
            self.__id = novo_id
        else:
            raise ValueError('Id inválido. O id deve ser um número inteiro.')
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str):
            raise ValueError('Nome inválido. O nome deve ser um texto.')
        elif not (3 <= len(novo_nome) <= 100):
            raise ValueError('O nome deve ter entre 3 e 100 caracteres.')
        self.__nome = novo_nome

    @property
    def email(self):
        return self.__email
        
    @email.setter
    def email(self, novo_email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(padrao, novo_email): 
            self.__email = novo_email
        else:
            raise ValueError('E-mail inválido. Verifique o formato: exemplo@dominio.com')
    
    @property
    def senha(self):
        return self.__senha
        
    @senha.setter
    def senha(self, nova_senha):
        if nova_senha.replace(' ', '').isalpha():
            raise ValueError("A senha deve conter um número ou caractere especial.")
        self.__senha = nova_senha

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "senha": self.__senha
        }

    def __str__(self):
        return f"Usuário {self.id}: {self.nome} ({self.email})"
    
class Usuarios(Persistencia):
    def __init__(self, arquivo: str):
        super().__init__(arquivo)

    def listar_id(self, id_usuario: int):
        usuarios = self.abrir()
        for u in usuarios:
            if u['id'] == id_usuario:
                return u
        return None
