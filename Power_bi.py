import streamlit as st
import base64
import os

# 🔐 Controle de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False

# 🔧 Função para definir imagem de fundo
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
        </style>
    """, unsafe_allow_html=True)

# 🖼️ Função para exibir foto do usuário
def exibir_foto(caminho):
    if os.path.exists(caminho):
        st.image(caminho, width=150)
    else:
        st.image("icones/padrao.png", width=150)

# 👥 Usuários simulados
usuarios = {
    "ceo_user": {"senha": "123", "cargo": "CEO", "nome": "Carlos", "foto": "ceo.png"},
    "gerente_user": {"senha": "789", "cargo": "GERENTE", "nome": "Samuel David Veiga", "foto": "gerente.png"},
}

# 🔗 Relatórios simulados
powerbi_links = {
    "Hierarquia": "https://app.powerbi.com/view?r=eyJrIjoiHIERARQUIA_ID",
    "Certificado": "https://app.powerbi.com/view?r=eyJrIjoiCERTIFICADO_ID",
    "LOG VT": "https://app.powerbi.com/view?r=eyJrIjoiLOGVT_ID",
    "geral": "https://app.powerbi.com/view?r=eyJrIjoiGERAL_ID"
}

# 🎨 Fundo
set_background("icones/Painel_power_point.png")

# 🔐 Tela de login
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

# 👤 Página após login
else:
    dados = usuarios[st.session_state.usuario]
    nome = dados["nome"]
    cargo = dados["cargo"]

    # 🔧 Layout com colunas: sidebar + conteúdo
    col1, col2 = st.columns([1, 4])

    with col1:
        st.markdown(f"""
            <div style="background-color: #2f2f2f; padding: 20px; height: 100vh;">
                <img src="icones/LOGO_MVVS_COLOR.png" width="120">
                <h3 style="color: white;">👤 Usuário</h3>
        """, unsafe_allow_html=True)
        exibir_foto(f"icones/{dados['foto']}")
        st.markdown(f"<p style='color:white;'>Bem-vindo, {nome}!</p>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color: #555;'>", unsafe_allow_html=True)

        st.markdown("<h4 style='color:white;'>📁 Relatórios</h4>", unsafe_allow_html=True)
        relatorio = st.radio("Selecione o relatório:", ["Hierarquia", "Certificado", "LOG VT"])

        st.markdown("<hr style='border-color: #555;'>", unsafe_allow_html=True)
        if st.button("🔒 Sair"):
            st.session_state.logado = False
            st.experimental_rerun()

    with col2:
        st.markdown(f"### 📊 Relatório: {relatorio}")
        st.components.v1.iframe(powerbi_links.get(relatorio, powerbi_links["geral"]), height=600, scrolling=True)


