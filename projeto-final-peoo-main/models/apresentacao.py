from datetime import datetime
from models.persistencia import Persistencia

class Apresentacao:
    def __init__(self, id: int, id_banda: int, data: datetime, local: str, confirmado: bool = False):
        self.id = id
        self.id_banda = id_banda
        self.data = data
        self.local = local
        self.confirmado = confirmado

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O ID deve ser um número inteiro.")
        self.__id = valor

    @property
    def id_banda(self):
        return self.__id_banda

    @id_banda.setter
    def id_banda(self, valor):
        if not isinstance(valor, int):
            raise ValueError("O ID da banda deve ser um número inteiro.")
        self.__id_banda = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        if not isinstance(valor, datetime):
            raise ValueError("Data inválida. Deve ser um objeto datetime.")
        self.__data = valor

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Local inválido. Informe um texto válido.")
        self.__local = valor.strip()

    @property
    def confirmado(self):
        return self.__confirmado

    @confirmado.setter
    def confirmado(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("O valor de 'confirmado' deve ser booleano.")
        self.__confirmado = valor

    def __str__(self):
        return (f"Apresentação {self.id} - Banda {self.id_banda} em "
                f"{self.data.strftime('%d/%m/%Y %H:%M')} no local {self.local}")

    def to_dict(self):
        return {
            "id": self.id,
            "id_banda": self.id_banda,
            "data": self.data.strftime("%Y-%m-%d %H:%M"),
            "local": self.local,
            "confirmado": self.confirmado
        }

    @staticmethod
    def from_dict(data: dict):
        return Apresentacao(
            id=data["id"],
            id_banda=data["id_banda"],
            data=datetime.strptime(data["data"], "%Y-%m-%d %H:%M"),
            local=data["local"],
            confirmado=data["confirmado"]
        )

class Apresentacoes(Persistencia):
    def inserir(self, apresentacao: Apresentacao):
        apresentacoes = self.abrir()
        apresentacoes.append(apresentacao.to_dict())
        self.salvar(apresentacoes)

    def listar(self):
        return [Apresentacao.from_dict(a) for a in self.abrir()]

    def listar_id(self, id_apresentacao: int):
        for a in self.abrir():
            if a["id"] == id_apresentacao:
                return Apresentacao.from_dict(a)
        return None

    def atualizar(self, id_apresentacao: int, novos_dados: dict):
        apresentacoes = self.abrir()
        for a in apresentacoes:
            if a["id"] == id_apresentacao:
                a.update(novos_dados)
        self.salvar(apresentacoes)

    def excluir(self, id_apresentacao: int):
        apresentacoes = [a for a in self.abrir() if a["id"] != id_apresentacao]
        self.salvar(apresentacoes)