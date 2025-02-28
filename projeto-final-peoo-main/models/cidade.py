import re
from models.persistencia import Persistencia

class Cidade:
    def __init__(self, id: int, nome: str, local_show: str, estado: str):
        self.id = id
        self.nome = nome
        self.local_show = local_show
        self.estado = estado

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        if isinstance(valor, int):
            self.__id = valor
        else:
            raise ValueError("O id da cidade deve ser um número inteiro.")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValueError("Nome inválido. A cidade deve ter pelo menos 2 caracteres.")
        self.__nome = valor.strip()

    @property
    def local_show(self):
        return self.__local_show

    @local_show.setter
    def local_show(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) == 0:
            raise ValueError("Local de show inválido. Informe um texto válido.")
        self.__local_show = valor.strip()

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise ValueError("Estado inválido. Informe pelo menos 2 caracteres.")
        self.__estado = valor.strip()

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "local_show": self.local_show,
            "estado": self.estado
        }

    def __str__(self):
        return f"Cidade {self.id}: {self.nome} - Local do show: {self.local_show} - Estado: {self.estado}"

class Cidades(Persistencia):
    def __init__(self, arquivo: str):
        super().__init__(arquivo)

    def listar_id(self, id_cidade: int):
        cidades = self.abrir()
        for c in cidades:
            if c['id'] == id_cidade:
                return c
        return None