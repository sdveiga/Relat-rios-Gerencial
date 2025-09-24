import streamlit as st
import base64
import os
import pandas as pd

# Simulação de usuários e senhas
usuarios = {
    "samuel": {"senha": "1234", "cargo": "Gerente"},
    "ana": {"senha": "abcd", "cargo": "Supervisor"},
    "joao": {"senha": "senha", "cargo": "Diretor"}
}

# Inicializa sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.cargo = ""

# Tela de login
if not st.session_state.logado:
    st.title("🔐 Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.session_state.cargo = usuarios[usuario]["cargo"]
            st.success(f"Bem-vindo, {usuario}!")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha inválidos.")

# Menu principal
if st.session_state.logado:
    st.sidebar.title("📋 Menu")
    menu = st.sidebar.selectbox("Escolha uma opção", ["📊 Indicadores", "📈 Relatório Power BI", "🚪 Sair"])

    if menu == "📊 Indicadores":
        st.markdown("## 📊 Indicadores")
        st.write("Aqui você pode visualizar os indicadores do sistema FCA.")
        # Você pode inserir aqui os gráficos ou tabelas que quiser

    elif menu == "📈 Relatório Power BI":
        st.markdown("## 📈 Relatório Power BI")
        st.write("Clique abaixo para abrir o relatório:")
        url_powerbi = "https://app.powerbi.com/view?r=SEU_LINK_AQUI"
        st.markdown(f"[🔗 Abrir relatório Power BI]({url_powerbi})", unsafe_allow_html=True)

    elif menu == "🚪 Sair":
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.session_state.cargo = ""
        st.experimental_rerun()
