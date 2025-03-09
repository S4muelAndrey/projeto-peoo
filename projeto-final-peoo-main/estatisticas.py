import matplotlib.pyplot as plt
import streamlit as st

def gerar_grafico_exemplo():
    fig, ax = plt.subplots()
    # Exemplo de dados:
    ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
    ax.set_title("Exemplo de Gráfico")
    return fig

def mostrar_grafico():
    st.title("Gráfico de Exemplo")
    fig = gerar_grafico_exemplo()
    st.pyplot(fig)

if __name__ == "__main__":
    mostrar_grafico()
