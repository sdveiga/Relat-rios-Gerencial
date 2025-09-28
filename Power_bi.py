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

# 🔧 Estilo personalizado para o menu lateral
st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #2f2f2f;
        color: white;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    .css-1v3fvcr {color: white !important;}
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

# 🖼️ Função para exibir foto do usuário
def exibir_foto(caminho):
    if os.path.exists(caminho):
        st.sidebar.image(caminho, width=150)
    else:
        st.sidebar.image("icones/padrao.png", width=150)

# 👥 Usuários simulados
usuarios = {
    "gerente_user": {
        "senha": "789", "cargo": "GERENTE", "nome": "Samuel David Veiga",
        "foto": "gerente.png", "admissao": "01/07/2008", "funcionarios": 360
    }
}

# 🎨 Fundo
set_background("icones/Painel_power_point.png")

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

    # 📁 Menu lateral com foto e boas-vindas
    exibir_foto(f"icones/{dados['foto']}")
    st.sidebar.markdown(f"### 👋 Bem-vindo, {nome}!")
    st.sidebar.markdown(f"**Cargo:** {cargo}")
    st.sidebar.markdown(f"**Admissão:** {dados['admissao']}")
    st.sidebar.markdown(f"**Funcionários:** {dados['funcionarios']}")

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 📁 Relatórios Disponíveis")

    relatorios = {
        "📊 Indicadores": {
            "📈 Hierarquia": "Hierarquia",
            "🎓 Certificado": "Certificado",
            "🚌 LOG VT": "LOG VT",
            "⚙️ Eficiência": "Eficiência",
            "📊 Produtividade": "Produtividade",
            "🏅 Pontuação": "Pontuação",
            "🧩 MESH": "MESH",
            "🧭 Rota Inicial": "Rota Inicial",
            "🚩 Rota Final": "Rota Final"
        },
        "💰 Financeiro": {
            "🏗️ Faturamento Instalação": "Faturamento Instalação",
            "🔧 Faturamento Manutenção": "Faturamento Manutenção",
            "💸 Desconto de revisita": "Desconto de revisita",
            "🏢 Faturamento MDU": "Faturamento MDU",
            "🛒 Faturamento Vendas": "Faturamento Vendas"
        },
        "⚙️ Processos Operacionais": {
            "📝 Realizar IVM": "Realizar IVM",
            "🚨 Processo disciplinar": "Processo disciplinar"
        }
    }

    # 🔘 Lista única de opções
    opcoes = []
    for categoria, itens in relatorios.items():
        opcoes.append(f"— {categoria} —")
        for label in itens:
            opcoes.append(label)

    selecionado_label = st.sidebar.radio("Selecione o relatório:", opcoes)

    for categoria, itens in relatorios.items():
        if selecionado_label in itens:
            selecionado = itens[selecionado_label]
            break
    else:
        selecionado = "geral"

    # 📈 Exibe o relatório
    st.markdown(f"### 📊 Relatório: {selecionado}")
    st.components.v1.iframe(powerbi_links[selecionado], height=600, scrolling=True)

    # 🚪 Logout
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Sair"):
        st.session_state.logado = False
        st.experimental_rerun()
