import streamlit as st
import matplotlib.pyplot as plt
from models.persistencia import Persistencia

class estatisticas:
    def gerar_grafico():
        persistencia = Persistencia("dados/agendamentos.json")
        agendamentos = persistencia.ler_dados()
    
        contagem = {}
        for agendamento in agendamentos:
            data = agendamento["data"]
            contagem[data] = contagem.get(data, 0) + 1
    
        fig, ax = plt.subplots()
        ax.bar(contagem.keys(), contagem.values())
        ax.set_xlabel("Data")
        ax.set_ylabel("Quantidade de Apresentações")
        ax.set_title("Quantidade de Apresentações por Dia")
    
        st.pyplot(fig)
    
    def mostrar_estatisticas():
        st.title("Estatísticas do Sistema")
        gerar_grafico()
    
    if __name__ == "__main__":
        mostrar_estatisticas()
