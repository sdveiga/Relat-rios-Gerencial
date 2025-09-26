import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import os

st.set_page_config(page_title="Painel FCA", layout="wide")
caminho_csv = "historico_fca.csv"

# 🔧 Fundo e logo
def set_background(png_file):
    with open(png_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            color: white;
        }}
        label {{ color: white !important; }}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        div.stButton > button:first-child {{
            background-color: #808080;
            color: white;
            border: none;
            padding: 0.5em 1em;
            border-radius: 5px;
        }}
        div.stButton > button:first-child:hover {{
            background-color: #696969;
        }}
        </style>
    """, unsafe_allow_html=True)

def show_logo(png_file):
    with open(png_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <div style="position: absolute; top: 10px; right: 10px; z-index: 100;">
            <img src="data:image/png;base64,{encoded}" width="150">
        </div>
    """, unsafe_allow_html=True)

def exibir_foto(caminho):
    if os.path.exists(caminho):
        st.image(caminho, width=150)
    else:
        st.image("icones/padrao.png", width=150)

# 👥 Usuários simulados
usuarios = {
    "ceo_user": {"senha": "123", "cargo": "CEO", "nome": "Carlos", "foto": "ceo.png"},
    "diretor_user": {"senha": "456", "cargo": "DIRETOR", "nome": "Fernanda", "foto": "diretor.png"},
    "gerente_user": {"senha": "789", "cargo": "GERENTE", "nome": "Samuel David Veiga", "foto": "gerente.png"},
    "coord_user": {"senha": "abc", "cargo": "COORDENADOR", "nome": "Luciana", "foto": "coord.png"},
    "sup_user": {"senha": "def", "cargo": "SUPERVISOR", "nome": "Rafael", "foto": "sup.png"},
    "cop_user": {"senha": "ghi", "cargo": "OPERADOR", "nome": "Ana", "foto": "cop.png"},
}

hierarquia = ["OPERADOR", "SUPERVISOR", "COORDENADOR", "GERENTE", "DIRETOR", "CEO"]

def pode_ver(cargo_atual, cargo_registro):
    return hierarquia.index(cargo_atual.upper()) > hierarquia.index(cargo_registro.upper())

set_background("icones/Painel_power_point.png")
show_logo("icones/LOGO_MVVS_COLOR.png")

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    st.markdown("<h1 style='text-align: center;'>PAINEL GERENCIAL</h1>", unsafe_allow_html=True)
    st.markdown("### 🔐 Login de Acesso")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            st.session_state.logado = True
            st.session_state.usuario = usuario
        else:
            st.error("❌ Usuário ou senha incorretos.")
if st.session_state.logado:
    dados = usuarios[st.session_state.usuario]
    cargo = dados["cargo"]
    nome = dados["nome"]

    col1, col2 = st.columns([1, 3])
    with col1:
        exibir_foto(f"icones/{dados['foto']}")
        st.success(f"✅ Bem-vindo, {nome}!")

    with col2:
        st.markdown(f"**Nome:** {nome}")
        st.markdown(f"**Cargo:** {cargo}")

    menu = st.sidebar.radio("📁 Menu", ["📊 Indicadores", "🔒 Sair"])

    if menu == "📊 Indicadores":
        st.markdown("## 📊 Indicadores")
        aba_fca = st.radio("Escolha uma opção:", ["🔧 Preenchimento FCA", "📈 Apresentação FCA"], horizontal=True)

        # Parte 3 e Parte 4 entram aqui

    elif menu == "🔒 Sair":
        st.session_state.logado = False
        st.experimental_rerun()
