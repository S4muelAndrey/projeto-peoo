import streamlit as st
import time
from views import View

class ConfirmarShowUI:
    @staticmethod
    def main():
        st.header("Confirmar Show")
        ConfirmarShowUI.confirmar()

    @staticmethod
    def confirmar():
        # Lista as apresentações não confirmadas, usando o atributo 'confirmado'
        apresentacoes = View.apresentacao_listar()
        nao_confirmadas = [a for a in apresentacoes if not a.confirmado]
        if not nao_confirmadas:
            st.write("Nenhum show pendente de confirmação.")
            return
        # Cria as opções usando os atributos dos objetos
        opcoes = {f"ID {a.id} - Banda {a.id_banda} em {a.data.strftime('%d/%m/%Y %H:%M')}": a for a in nao_confirmadas}
        opcao = st.selectbox("Selecione o show para confirmar", list(opcoes.keys()), key="confirma_show")
        show = opcoes[opcao]
        if st.button("Confirmar Show"):
            View.apresentacao_atualizar(show.id, {"confirmado": True})
            st.success("Show confirmado!")
            time.sleep(2)
            st.rerun()
