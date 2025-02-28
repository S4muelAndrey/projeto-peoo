from datetime import datetime
from models.banda import Banda
from models.representante import Representante
from models.usuario import Usuario
from models.cidade import Cidade
from models.apresentacao import Apresentacao
from models.persistencia import Persistencia

def testar_bandas():
    print("📝 TESTANDO BANDAS 📝")
    
    banda_teste = Banda(1, 2, "Banda X", "bandeirantes", "rock", "nalice123@gmail.com", "alice@123", "(84) 99965-5932")
    persistencia = Persistencia("dados/dados_agenda.json")
    
    persistencia.salvar([banda_teste.to_dict()])
    print(f"📥 Banda adicionada:\n{banda_teste}")
    
    banda_teste.nome = "Banda Y"
    banda_teste.genero = "pop"
    persistencia.salvar([banda_teste.to_dict()])
    print(f"\n✍️ Banda atualizada:\n{banda_teste}")
    
    persistencia.salvar([])  # Simulando exclusão
    print("\n🗑️ Banda removida:")
    print("Nenhuma banda registrada.\n")

def testar_representantes():
    print("🕴️ TESTANDO REPRESENTANTES 🕴️")
    
    representante_teste = Representante(1, "Carlos", "carlinhos267@hotmail.com", "socorro.123", "(21) 98876-0991")
    persistencia = Persistencia("dados/dados_agenda.json")
    
    persistencia.salvar([representante_teste.to_dict()])
    print(f"📥 Representante adicionado:\n{representante_teste}")
    
    representante_teste.nome = "Carlos Silva"
    persistencia.salvar([representante_teste.to_dict()])
    print(f"\n✍️ Representante atualizado:\n{representante_teste}")
    
    persistencia.salvar([])  # Simulando exclusão
    print("\n🗑️ Representante removido:")
    print("Nenhum representante registrado.\n")

def testar_usuarios():
    print("👤 TESTANDO USUÁRIOS 👤")
    
    usuario_teste = Usuario(1, "João", "joao@email.com", "juarez47*")
    persistencia = Persistencia("dados/dados_agenda.json")
    
    persistencia.salvar([usuario_teste.to_dict()])
    print(f"📥 Usuário adicionado:\n{usuario_teste}")
    
    usuario_teste.email = "joaonovo@email.com"
    persistencia.salvar([usuario_teste.to_dict()])
    print(f"\n✍️ Usuário atualizado:\n{usuario_teste}")
    
    persistencia.salvar([])  # Simulando exclusão
    print("\n🗑️ Usuário removido:")
    print("Nenhum usuário registrado.\n")

def testar_cidades():
    print("🌆 TESTANDO CIDADES 🌆")
    
    cidade_teste = Cidade(1, "Natal", "Arena das Dunas", "RN")
    persistencia = Persistencia("dados/dados_agenda.json")
    
    persistencia.salvar([cidade_teste.to_dict()])
    print(f"📥 Cidade adicionada:\n{cidade_teste}")
    
    cidade_teste.nome = "São Paulo"
    persistencia.salvar([cidade_teste.to_dict()])
    print(f"\n✍️ Cidade atualizada:\n{cidade_teste}")
    
    persistencia.salvar([])  # Simulando exclusão
    print("\n🗑️ Cidade removida:")
    print("Nenhuma cidade registrada.\n")

def testar_apresentacoes():
    print("🎤 TESTANDO APRESENTAÇÕES 🎤")
    
    apresentacao_teste = Apresentacao(1, 1, datetime(2025, 5, 10, 20, 0), "Arena das Dunas", True)
    persistencia = Persistencia("dados/dados_agenda.json")
    
    persistencia.salvar([apresentacao_teste.to_dict()])
    print(f"📥 Apresentação adicionada:\n{apresentacao_teste}")
    
    apresentacao_teste.local = "Morumbi"
    persistencia.salvar([apresentacao_teste.to_dict()])
    print(f"\n✍️ Apresentação atualizada:\n{apresentacao_teste}")
    
    persistencia.salvar([]) 
    print("\n🗑️ Apresentação removida:")
    print("Nenhuma apresentação registrada.\n")

def main():
    testar_bandas()
    testar_representantes()
    testar_usuarios()
    testar_cidades()
    testar_apresentacoes()

if __name__ == "__main__":
    main()
    print("🎉 TESTES FINALIZADOS COM SUCESSO! 🎉")