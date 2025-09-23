import streamlit as st
import base64
import os

# 🔧 Oculta barra superior e rodapé
st.markdown("""
    <style>
    footer, header {visibility: hidden;}
    .menu-container {
        position: fixed;
        top: 80px;
        left: 0;
        width: 220px;
        height: 100%;
        background-color: rgba(0,0,0,0.6);
        padding: 20px;
        overflow-y: auto;
        z-index: 99;
        color: white;
    }
    .menu-container h3 {
        margin-top: 0;
        color: #fff;
    }
    .menu-container button {
        width: 100%;
        margin: 5px 0;
        background-color: #444;
        color: white;
        border: none;
        padding: 8px;
        border-radius: 5px;
        text-align: left;
    }
    .menu-container button:hover {
        background-color: #666;
    }
    .main-content {
        margin-left: 240px;
        padding: 20px;
    }
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
    "gerente_user": {"senha": "789", "cargo": "GESTOR TI", "nome": "Samuel David Veiga", "foto": "gerente.png", "admissao": "10/07/2023", "funcionarios": 330}
}

# 🔗 Relatórios simulados
powerbi_links = {
    "Indicadores": "https://app.powerbi.com/view?r=eyJrIjoiINDICADORES_ID",
    "Hierarquia": "https://app.powerbi.com/view?r=eyJrIjoiHIERARQUIA_ID",
    "Conectividade": "https://app.powerbi.com/view?r=eyJrIjoiCONECTIVIDADE_ID",
    "LOG IVTI": "https://app.powerbi.com/view?r=eyJrIjoiLOGIVTI_ID",
    "Eficiência": "https://app.powerbi.com/view?r=eyJrIjoiEFICIENCIA_ID",
    "Produtividade": "https://app.powerbi.com/view?r=eyJrIjoiPRODUTIVIDADE_ID",
    "Monitoramento": "https://app.powerbi.com/view?r=eyJrIjoiMONITORAMENTO_ID",
    "MESH": "https://app.powerbi.com/view?r=eyJrIjoiMESH_ID",
    "Rota Inicial": "https://app.powerbi.com/view?r=eyJrIjoiROTAINICIAL_ID",
    "Rota Final": "https://app.powerbi.com/view?r=eyJrIjoiROTAFINAL_ID",
    "Financeiro": "https://app.powerbi.com/view?r=eyJrIjoiFINANCEIRO_ID",
    "Faturamento": "https://app.powerbi.com/view?r=eyJrIjoiFATURAMENTO_ID",
    "Instalação": "https://app.powerbi.com/view?r=eyJrIjoiINSTALACAO_ID",
    "Faturamento novo": "https://app.powerbi.com/view?r=eyJrIjoiFATNOVO_ID"
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
    cargo = dados["cargo"]

    # 🧍 Informações do usuário
    col1, col2 = st.columns([1, 2])
    with col1:
        exibir_foto(f"icones/{dados['foto']}")
        st.markdown(f"<div style='margin-top: 10px; font-size: 18px;'>✅ Bem-vindo, <strong>{nome}</strong>!</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div style='line-height: 2; font-size: 16px;'>
                <strong>Nome:</strong> {nome}<br>
                <strong>Cargo:</strong> {cargo}<br>
                <strong>Data de Admissão:</strong> {dados['admissao']}<br>
                <strong>Funcionários na área:</strong> {dados['funcionarios']}
            </div>
        """, unsafe_allow_html=True)

    # 📁 Menu lateral fixo
    st.markdown("<div class='menu-container'><h3>📁 Relatórios</h3>", unsafe_allow_html=True)
    for nome_relatorio in powerbi_links.keys():
        if st.button(nome_relatorio, key=nome_relatorio):
            st.session_state.selecionado = nome_relatorio
    st.markdown("</div>", unsafe_allow_html=True)

    # 📊 Conteúdo principal
    st.markdown("<div class='main-content'>", unsafe_allow_html=True)
    relatorio = st.session_state.get("selecionado", "Indicadores")
    st.markdown(f"### 📊 Relatório: {relatorio}")
    st.components.v1.iframe(powerbi_links[relatorio], height=600, scrolling=True)
    st.markdown("</div>", unsafe_allow_html=True)


    # 🚪 Botão de logout dentro do menu lateral
    st.markdown("<div class='menu-container'>", unsafe_allow_html=True)
    if st.button("🔒 Sair"):
        st.session_state.logado = False
        st.session_state.selecionado = "Indicadores"
        st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)
