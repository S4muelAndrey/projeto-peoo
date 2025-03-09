from templates.abriragendaUI import AbrirAgendaUI
from templates.agendashowUI import AgendaShowUI
from templates.agendasshowsUI import AgendaShowsUI
from templates.confirmarshowUI import ConfirmarShowUI
from templates.loginUI import LoginUI
from templates.manterapresentacaoUI import ManterApresentacaoUI
from templates.manterbandaUI import ManterBandaUI
from templates.mantercidadeUI import ManterCidadeUI
from templates.manterrepresentanteUI import ManterRepresentanteUI
from templates.registerUI import RegisterUI
import streamlit as st
import time

class Index:
    @staticmethod
    def main():
        # Inicializa as variáveis de sessão se não existirem
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        if 'user_type' not in st.session_state:
            st.session_state.user_type = None
        if 'user_name' not in st.session_state:
            st.session_state.user_name = ''
        if "login_sucesso" not in st.session_state:
            st.session_state["login_sucesso"] = False

        if not st.session_state["login_sucesso"]:
            menu = st.sidebar.selectbox("Menu", [
                "Login",
                "Registrar"
            ], key="menu-sidebar")
            if menu == "Login":
                LoginUI.main()
            elif menu == "Registrar":
                RegisterUI.main()
        else:
            # Verifica o tipo de usuário para exibir o menu adequado
            if st.session_state.user_type == "Admin":
                menu = st.sidebar.selectbox("Menu", [
                    "Manter Cidade",
                    "Manter Banda",
                    "Manter Apresentação",
                    "Manter Representante"
                ], key="menu-sidebar")
                if menu == "Manter Cidade":
                    ManterCidadeUI.main()
                elif menu == "Manter Banda":
                    ManterBandaUI.main()
                elif menu == "Manter Apresentação":
                    ManterApresentacaoUI.main()
                elif menu == "Manter Representante":
                    ManterRepresentanteUI.main()
            else:
                menu = st.sidebar.selectbox("Menu", [
                    "Abrir Agenda",
                    "Confirmar Show",
                    "Agendar Show",
                    "Agenda de Shows"
                ], key="menu-sidebar")
                if menu == "Abrir Agenda":
                    AbrirAgendaUI.main()
                elif menu == "Confirmar Show":
                    ConfirmarShowUI.main()
                elif menu == "Agendar Show":
                    AgendaShowUI.main()
                elif menu == "Agenda de Shows":
                    AgendaShowsUI.main()
            if st.sidebar.button("Sair"):
                st.session_state["login_sucesso"] = False
                st.session_state.clear()
                st.session_state["login_sucesso"] = False
                st.rerun()
