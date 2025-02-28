import streamlit as st
import time
from templates.registerUI import RegisterUI
from templates.loginUI import LoginUI
from templates.mantercidadeUI import ManterCidadeUI
from templates.manterbandaUI import ManterBandaUI
from templates.manterapresentacaoUI import ManterApresentacaoUI
from templates.manterrepresentanteUI import ManterRepresentanteUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.confirmarshowUI import ConfirmarShowUI
from templates.agendashowUI import AgendaShowUI
from templates.agendasshowsUI import AgendaShowsUI

class Index:
    @staticmethod
    def main():
        if "login_sucesso" not in st.session_state or not st.session_state["login_sucesso"]:
            menu = st.sidebar.selectbox("Menu", [
                "Login",
                "Registrar"
            ], key="menu-sidebar")

            if menu == "Login":
                LoginUI.main()
            elif menu == "Registrar":
                RegisterUI.main()
        else:
            menu = st.sidebar.selectbox("Menu", [
                "Manter Cidade",
                "Manter Banda",
                "Manter Apresentação",
                "Manter Representante",
                "Abrir Agenda",
                "Confirmar Show",
                "Agendar Show",
                "Agenda de Shows"
            ], key="menu-sidebar")

            if menu == "Manter Cidade":
                ManterCidadeUI.main()
            elif menu == "Manter Banda":
                ManterBandaUI.main()
            elif menu == "Manter Apresentação":
                ManterApresentacaoUI.main()
            elif menu == "Manter Representante":
                ManterRepresentanteUI.main()
            elif menu == "Abrir Agenda":
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
