import streamlit as st
from controllers.auth_controller import AuthController

def render_login():
    st.title('Login')
    email = st.text_input('Email')
    password = st.text_input('Senha', type='password')
    if st.button('Entrar'):
        try:
            user = AuthController.login(email, password)
            st.session_state.authenticated = True
            st.session_state.user_type = user['user_type']
            st.session_state.user_name = user['name']
            st.success(f'Bem-vindo, {user["name"]}!')
            st.experimental_rerun()
        except ValueError as e:
            st.error(str(e))

def render_register():
    st.title('Cadastro')
    name = st.text_input('Nome')
    email = st.text_input('Email')
    password = st.text_input('Senha', type='password')
    user_type = st.selectbox('Tipo de usuário', ['Banda', 'Representante', 'Admin'])
    if st.button('Cadastrar'):
        try:
            message = AuthController.register(name, email, password, user_type)
            st.success(message)
            st.experimental_rerun()
        except ValueError as e:
            st.error(str(e))
