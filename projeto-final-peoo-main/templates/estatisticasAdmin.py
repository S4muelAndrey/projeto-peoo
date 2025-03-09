import streamlit as st
import matplotlib.pyplot as plt
from models.persistencia import Persistencia

def gerar_grafico_agendamentos():
    # Lê os dados do arquivo de agendamentos
    persistencia = Persistencia("dados/agendamentos.json")
    agendamentos = persistencia.abrir()
    if not agendamentos:
        st.write("Nenhum agendamento registrado.")
        return None

    # Conta quantos agendamentos existem por data
    contagem = {}
    for agendamento in agendamentos:
        # Supondo que o campo "data" esteja no formato "dd/mm/YYYY HH:MM" ou "dd/mm/YYYY"
        data = agendamento.get("data", "Sem data")
        contagem[data] = contagem.get(data, 0) + 1

    # Cria um gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(list(contagem.keys()), list(contagem.values()))
    ax.set_xlabel("Data")
    ax.set_ylabel("Quantidade de Agendamentos")
    ax.set_title("Agendamentos por Data")
    return fig

def main():
    st.header("Estatísticas de Agendamentos")
    fig = gerar_grafico_agendamentos()
    if fig:
        st.pyplot(fig)

if __name__ == "__main__":
    main()
