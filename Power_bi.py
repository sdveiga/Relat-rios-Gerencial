import streamlit as st
import base64
import os

# 🔧 Oculta barra superior e rodapé do Streamlit
st.markdown("""
    <style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    section[data-testid="stSidebar"] {
        background-color: #2f2f2f;
        color: white;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    .css-1v3fvcr {color: white !important;}
    div[data-testid="stSidebarCollapseButton"] {
        display: none !important;
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
    nome = dados["nome"]
    cargo = dados["cargo"]

    # 📁 Menu lateral com foto e boas-vindas
    exibir_foto(f"icones/{dados['foto']}")
    st.sidebar.markdown(f"### 👋 Bem-vindo, {nome}!")
    st.sidebar.markdown(f"**Cargo:** {cargo}")

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
    opcoes.append("📋 ICG")  # 👈 Nova visão adicionada

    selecionado_label = st.sidebar.radio("Selecione o relatório:", opcoes)

    for categoria, itens in relatorios.items():
        if selecionado_label in itens:
            selecionado = itens[selecionado_label]
            break
    else:
        selecionado = "geral"

    # 📈 Exibe o relatório
    if selecionado_label != "📋 ICG":
        st.markdown(f"### 📊 Relatório: {selecionado}")
        st.components.v1.iframe(powerbi_links[selecionado], height=600, scrolling=True)

    # 📋 Visão ICG
    elif selecionado_label == "📋 ICG":
        st.markdown("### 📋 Indicadores de Controle de Gestão (ICG)")

        indicador = st.text_input("🔢 Indicador")
        mes = st.selectbox("🗓️ Mês", [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ])
        
        nota = st.number_input("📈 Nota", min_value=0.0, max_value=10.0, step=0.1)

        st.markdown("#### 🗓️ Acompanhamento Semanal")
        ofensores = [st.text_input(f"Ofensor Semana {i+1}") for i in range(5)]

        st.markdown("#### 📊 Parreto")
        col1, col2 = st.columns(2)
        with col1:
            parreto1 = st.text_input("1º Parreto")
            impacto1 = st.number_input("Impacto % (1º)", min_value=0, max_value=100)
        with col2:
            parreto2 = st.text_input("2º Parreto")
            impacto2 = st.number_input("Impacto % (2º)", min_value=0, max_value=100)

        st.markdown("#### 🧠 FCA")
        fato = st.text_area("📝 Fato")
        causa = st.text_area("🧪 Causa")
        acao = st.text_area("✅ Ação")

        st.markdown("#### 📎 Evidências")
        evidencia = st.text_area("📌 Observações ou link de imagem")

        if st.button("💾 Salvar Indicador"):
            st.success("✅ Indicador registrado com sucesso!")
            # Aqui podemos salvar em session_state ou banco de dados futuramente

    # 🚪 Logout
    st.sidebar.markdown("---")
    if st.sidebar.button("🔒 Sair"):
        st.session_state.logado = False
        st.experimental_rerun()
        

