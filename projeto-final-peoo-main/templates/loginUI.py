import streamlit as st
import time
from views import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("E-mail", key="login_email")
        senha = st.text_input("Senha", key="login_senha", type="password")
        if st.button("Entrar"):
            # Verifica se as credenciais correspondem ao admin
            if email == "admin@adm.com" and senha == "SenhaDoAdmin":
                st.session_state["usuario_id"] = 0  # ID fixo para admin
                st.session_state["usuario_nome"] = "Administrador"
                st.session_state["login_sucesso"] = True 
                st.session_state["user_type"] = "Admin"
                st.success("Login efetuado com sucesso!")
                time.sleep(2)
                st.rerun()
            else:
                # Verifica login para usuários normais ou representantes
                usuario_encontrado = None
                for u in View.usuario_listar():
                    if u['email'] == email and u['senha'] == senha:
                        usuario_encontrado = u
                        break
                if not usuario_encontrado:
                    for r in View.representante_listar():
                        if r['email'] == email and r['senha'] == senha:
                            usuario_encontrado = r
                            break
                if usuario_encontrado:
                    st.session_state["usuario_id"] = usuario_encontrado["id"]
                    st.session_state["usuario_nome"] = usuario_encontrado["nome"]
                    st.session_state["login_sucesso"] = True 
                    st.session_state["user_type"] = usuario_encontrado.get("user_type", "User")
                    st.success("Login efetuado com sucesso!")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("E-mail ou senha inválidos.")
