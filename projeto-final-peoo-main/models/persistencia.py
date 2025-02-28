import json


class Persistencia:
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
    
    def salvar(self, dados):
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f, indent=4)
    
    def abrir(self):
        try:
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def inserir(self, dado):
        dados = self.abrir()
        dados.append(dado.to_dict())
        self.salvar(dados)
    
    def listar(self):
        return self.abrir()
    
    def excluir(self, id_dado):
        dados = self.abrir()
        dados = [d for d in dados if d['id'] != id_dado]
        self.salvar(dados)
    
    def atualizar(self, id_dado, novos_dados):
        dados = self.abrir()
        for d in dados:
            if d['id'] == id_dado:
                d.update(novos_dados)
        self.salvar(dados)