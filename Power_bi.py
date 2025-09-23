import streamlit as st
import base64
import os

# 🔧 Oculta barra superior e rodapé do Streamlit
st.markdown("""
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

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
        label {{ color: white !important; }}
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

# 🖼️ Função para exibir logo
def show_logo(png_file):
    with open(png_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <div style="position: absolute; top: 10px; right: 10px; z-index: 100;">
            <img src="data:image/png;base64,{encoded}" width="150">
        </div>
    """, unsafe_allow_html=True)

# 🖼️ Função para exibir foto do usuário
def exibir_foto(caminho):
    if os.path.exists(caminho):
        st.image(caminho, width=150)
    else:
        st.image("icones/padrao.png", width=150)

# 👥 Usuários simulados
usuarios = {
    "gerente_user": {"senha": "789", "nome": "Samuel David Veiga", "foto": "gerente.png"},
    # outros usuários podem ser adicionados aqui
}

# 🎨 Fundo e logo
set_background("icones/Painel_power_point.png")
show_logo("icones/LOGO_MVVS_COLOR.png")

# 🔐 Controle de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False

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

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Painel de Boas-Vindas</h2>", unsafe_allow_html=True)

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    exibir_foto(f"icones/{dados['foto']}")
    st.success(f"✅ Bem-vindo, {nome}!")
    st.markdown("</div>", unsafe_allow_html=True)

    # 🚪 Botão de logout
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Sair"):
        st.session_state.logado = False
        st.experimental_rerun()
