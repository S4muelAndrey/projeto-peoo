import json
import re
from models.usuario import Usuario
from models.representante import Representante
from models.persistencia import Persistencia

class Banda:
    def __init__(self, id: int, id_representante: int, nome: str, gravadora: str, genero: str, email: str, senha: str, tel: str):
        self.id = id
        self.id_representante = id_representante
        self.nome = nome
        self.gravadora = gravadora
        self.genero = genero        
        self.email = email        
        self.senha = senha        
        self.tel = tel

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
    def id_representante(self):
        return self.__idr
    
    @id_representante.setter
    def id_representante(self, novo_idr):
        if isinstance(novo_idr, int):
            self.__idr = novo_idr
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
            raise ValueError('O nome da banda deve ter, no mínimo, 3 caracteres e, no máximo, 100 caracteres.')
        else:
            self.__nome = novo_nome

    @property
    def gravadora(self):
        return self.__gravadora
    
    @gravadora.setter
    def gravadora(self, nova_gravadora):
        if not isinstance(nova_gravadora, str):
            raise ValueError('Nome da gravadora inválido. O nome dela deve ser um texto.')
        else:
            self.__gravadora = nova_gravadora

    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, novo_genero):
        if not isinstance(novo_genero, str):
            raise ValueError('Nome do gênero inválido. O nome deve ser um texto.')
        else:
            self.__genero = novo_genero

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
    
    @property
    def tel(self):
        return self.__tel
    
    @tel.setter
    def tel(self, novo_telefone):
        padrao = r'^\(\d{2}\)\s?9\d{4}-\d{4}$|^\(\d{2}\)\s?\d{4}-\d{4}$'
        if re.match(padrao, novo_telefone):
            self.__tel = novo_telefone
        else:
            raise ValueError('O número de telefone no padrão correto. Verifique se o formato é esse: (00) 0000-0000 para fixos, (00) 90000-0000 para celulares.')

    def to_dict(self):
        return {
            "id": self.__id, 
            "id_representante": self.__idr,  
            "nome": self.__nome, 
            "gravadora": self.__gravadora, 
            "genero": self.__genero, 
            "email": self.__email, 
            "senha": self.__senha, 
            "tel": self.__tel
        }

    def __str__(self):
        return f"Banda {self.id}: {self.nome} - {self.genero} (Gravadora: {self.gravadora})"

class Bandas(Persistencia):
    def __init__(self, arquivo: str):
        super().__init__(arquivo)

    def listar_id(self, id_banda: int):
        bandas = self.abrir()
        for b in bandas:
            if b['id'] == id_banda:
                return b
        return None