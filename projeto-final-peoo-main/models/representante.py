import re
from models.usuario import Usuario
from models.persistencia import Persistencia

class Representante(Usuario):
    def __init__(self, id: int, nome: str, email: str, senha: str, telefone: str):
        super().__init__(id, nome, email, senha)
        self.telefone = telefone

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        padrao = r'^\(\d{2}\)\s?9\d{4}-\d{4}$|^\(\d{2}\)\s?\d{4}-\d{4}$'
        if re.match(padrao, novo_telefone):
            self.__telefone = novo_telefone
        else:
            raise ValueError("Telefone inválido.")
    
    def to_dict(self):
        data = super().to_dict()
        data["telefone"] = self.__telefone
        return data

    def __str__(self):
        return f"Representante {self.id}: {self.nome} ({self.email}, {self.telefone})"
    
class Representantes(Persistencia):
    def __init__(self, arquivo: str):
        super().__init__(arquivo)

    def listar_id(self, id_representante: int):
        representantes = self.abrir()
        for r in representantes:
            if r['id'] == id_representante:
                return r
        return None