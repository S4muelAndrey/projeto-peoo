import streamlit as st
import time
from views import View

class RegisterUI:
    @staticmethod
    def main():
        st.header("Registrar Novo Usuário")
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        
        if st.button("Registrar"):
            RegisterUI.insert(nome, email, senha)
            st.success("Registro efetuado com sucesso!")
            time.sleep(2)
            st.session_state["login_sucesso"] = True 
            st.rerun() 

    @staticmethod
    def insert(nome: str, email: str, senha: str):
        View.usuario_inserir(nome, email, senha)
