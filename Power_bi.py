import streamlit as st
import base64
import os

# 🔧 Oculta barra superior e rodapé do Streamlit

st.markdown("""
    <style>

    /* Estiliza a sidebar */
    [data-testid="stSidebar"] {
        background-color: #2f2f2f;
        color: white;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    [data-testid="stSidebar"] .stMarkdown {
        text-align: center;
    }

    [data-testid="stSidebar"] .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
    }

    /* Oculta o botão de recolher da sidebar */
    [data-testid="collapsedControl"] {
        visibility: hidden !important;
        height: 0px !important;
        width: 0px !important;
        overflow: hidden !important;
        position: absolute !important;
        top: -1000px !important;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Oculta o botão de recolher da sidebar */
    div[data-testid="collapsedControl"] {
        visibility: hidden !important;
        display: none !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
        z-index: -1 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Oculta o ícone de recolher da sidebar */
    span.st-emotion-cache-pd6qx2.ejhh0er0 {
        display: none !important;
        visibility: hidden !important;
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

st.markdown("""
    <style>
    /* Oculta o ícone de recolher da sidebar e seu contêiner */
    span.st-emotion-cache-189uypx.e1t4gh342,
    span.st-emotion-cache-pd6qx2.ejhh0er0 {
        display: none !important;
        visibility: hidden !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
        z-index: -1 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Oculta o botão de recolher da sidebar e todos seus elementos */
    div[data-testid="stSidebarCollapseButton"],
    button[data-testid="stBaseButton-headerNoPadding"],
    span.st-emotion-cache-189uypx.e1t4gh342,
    span.st-emotion-cache-pd6qx2.ejhh0er0 {
        display: none !important;
        visibility: hidden !important;
        position: absolute !important;
        top: -9999px !important;
        left: -9999px !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
        z-index: -1 !important;
    }
    </style>
""", unsafe_allow_html=True)



# 🖼️ Função para exibir foto do usuário
def exibir_foto(caminho, sidebar=False):
    if os.path.exists(caminho):
        if sidebar:
            st.sidebar.image(caminho, width=150)
        else:
            st.image(caminho, width=150)
    else:
        if sidebar:
            st.sidebar.image("icones/padrao.png", width=150)
        else:
            st.image("icones/padrao.png", width=150)

# 👥 Usuários simulados
usuarios = {
    "ceo_user": {"senha": "123", "cargo": "CEO", "nome": "Carlos", "foto": "ceo.png", "admissao": "01/01/2015", "funcionarios": 120},
    "diretor_user": {"senha": "456", "cargo": "DIRETOR", "nome": "Fernanda", "foto": "diretor.png", "admissao": "15/03/2016", "funcionarios": 80},
    "gerente_user": {"senha": "789", "cargo": "GERENTE", "nome": "Samuel David Veiga", "foto": "gerente.png", "admissao": "01/07/2008", "funcionarios": 360},
    "coord_user": {"senha": "abc", "cargo": "COORDENADOR", "nome": "Luciana", "foto": "coord.png", "admissao": "20/09/2019", "funcionarios": 15},
    "sup_user": {"senha": "def", "cargo": "SUPERVISOR", "nome": "Rafael", "foto": "sup.png", "admissao": "05/11/2020", "funcionarios": 8},
    "cop_user": {"senha": "ghi", "cargo": "OPERADOR COP", "nome": "Ana", "foto": "cop.png", "admissao": "12/01/2022", "funcionarios": 0},
}

# 🔗 Relatórios Power BI simulados
powerbi_links = {
    "Hierarquia": "https://app.powerbi.com/view?r=eyJrIjoiMGRiZWNjNWEtNDZiNS00Yjc2LWFjZGEtYzIxMWU4MDI5YTBkIiwidCI6ImY0OGYxNzE0LTYyYTUtNGM4MS1iYjVmLTJiZmExYjBmNGI4MSJ9",
    "Certificado": "https://app.powerbi.com/view?r=eyJrIjoiCERTIFICADO_ID",
    "LOG VT": "https://app.powerbi.com/view?r=eyJrIjoiLOGVT_ID",
    "Eficiência": "https://app.powerbi.com/view?r=eyJrIjoiEFICIENCIA_ID",
    "Produtividade": "https://app.powerbi.com/view?r=eyJrIjoiPRODUTIVIDADE_ID",
    "Pontuação": "https://app.powerbi.com/view?r=eyJrIjoiPONTUACAO_ID",
    "MESH": "https://app.powerbi.com/view?r=eyJrIjoiMESH_ID",
    "Rota Inicial": "https://app.powerbi.com/view?r=eyJrIjoiROTA_INICIAL_ID",
    "Rota Final": "https://app.powerbi.com/view?r=eyJrIjoiROTA_FINAL_ID",
    "Faturamento Instalação": "https://app.powerbi.com/view?r=eyJrIjoiFAT_INST_ID",
    "Faturamento Manutenção": "https://app.powerbi.com/view?r=eyJrIjoiFAT_MAN_ID",
    "Desconto de revisita": "https://app.powerbi.com/view?r=eyJrIjoiDESCONTO_ID",
    "Faturamento MDU": "https://app.powerbi.com/view?r=eyJrIjoiFAT_MDU_ID",
    "Faturamento Vendas": "https://app.powerbi.com/view?r=eyJrIjoiFAT_VENDAS_ID",
    "Produção por equipe": "https://app.powerbi.com/view?r=eyJrIjoiPROD_EQUIPE_ID",
    "Realizar IVM": "https://app.powerbi.com/view?r=eyJrIjoiIVM_ID",
    "Processo disciplinar": "https://app.powerbi.com/view?r=eyJrIjoiDISCIPLINAR_ID",
    "geral": "https://app.powerbi.com/view?r=eyJrIjoiMGRiZWNjNWEtNDZiNS00Yjc2LWFjZGEtYzIxMWU4MDI5YTBkIiwidCI6ImY0OGYxNzE0LTYyYTUtNGM4MS1iYjVmLTJiZmExYjBmNGI4MSJ9"
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
    cargo = dados["cargo"]
    nome = dados["nome"]

    # 👤 Sidebar com logo, foto e saudação
    with st.sidebar:
        st.image("icones/LOGO_MVVS_COLOR.png", width=120)
        st.markdown("## 👤 Usuário")
        exibir_foto(f"icones/{dados['foto']}", sidebar=True)
        st.success(f"Bem-vindo, {nome}!")
        st.markdown("## 📁 Relatórios Disponíveis")

        # 📁 Menu lateral com relatórios
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
        } if cargo in ["CEO", "GERENTE", "COORDENADOR"] else {},
        "⚙️ Processos Operacionais": {
            "📝 Realizar IVM": "Realizar IVM",
            "🚨 Processo disciplinar": "Processo disciplinar"
        }
            }  # fim do dicionário de relatórios

        # 🔘 Lista única de opções
        opcoes = []
        for categoria, itens in relatorios.items():
            if itens:
                opcoes.append(f"— {categoria} —")
                for label, chave in itens.items():
                    opcoes.append(label)

        # 🔘 Seleção única
        selecionado_label = st.radio("Selecione o relatório:", opcoes)

        # 🔍 Mapeia o item selecionado para a chave do relatório
        for categoria, itens in relatorios.items():
            if selecionado_label in itens:
                selecionado = itens[selecionado_label]
                break
        else:
            selecionado = "geral"

        # 🚪 Botão de logout
        st.markdown("---")
        if st.button("🔒 Sair"):
            st.session_state.logado = False
            st.experimental_rerun()

    # 📈 Exibe o relatório correspondente no corpo principal
    st.markdown(f"### 📊 Relatório: {selecionado}")
    st.components.v1.iframe(powerbi_links[selecionado], height=600, scrolling=True)


















