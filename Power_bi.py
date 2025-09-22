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

# 🎨 Fundo e logo
set_background("icones/Painel_power_point.png")
show_logo("icones/LOGO_MVVS_COLOR.png")

# 🔐 Controle de sessão
if "logado" not in st.session_state:
    st.session_state.logado = False

if "menu_ocultado" not in st.session_state:
    st.session_state.menu_ocultado = False

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

    col1, col2 = st.columns([1, 3])
    with col1:
        exibir_foto(f"icones/{dados['foto']}")
        st.success(f"✅ Bem-vindo, {nome}!")

    with col2:
        st.markdown(f"**Nome:** {nome}")
        st.markdown(f"**Cargo:** {cargo}")
        st.markdown(f"**Data de Admissão:** {dados['admissao']}")
        st.markdown(f"**Funcionários Abaixo:** {dados['funcionarios']}")

    # 🔘 Botão para ocultar menu (irreversível)
    if not st.session_state.menu_ocultado:
        if st.button("❌ Ocultar Menu Lateral"):
            st.session_state.menu_ocultado = True

    # 📁 Menu lateral condicional
    if not st.session_state.menu_ocultado:
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
            
                   }

        opcoes = []
        for categoria, itens in relatorios.items():
            if itens:
                opcoes.append(f"— {categoria} —")
                for label, chave in itens.items():
                    opcoes.append(label)

        selecionado_label = st.sidebar.radio("Selecione o relatório:", opcoes)

        for categoria, itens in relatorios.items():
            if selecionado_label in itens:
                selecionado = itens[selecionado_label]
                break
        else:
            selecionado = "geral"

        st.sidebar.markdown("---")
        if st.sidebar.button("🔒 Sair"):
            st.session_state.logado = False
            st.experimental_rerun()
    else:
        # Se o menu foi ocultado, exibe o relatório padrão
        selecionado = "geral"

    # 📈 Exibe o relatório correspondente
    st.markdown(f"### 📊 Relatório: {selecionado}")
    st.components.v1.iframe(powerbi_links[selecionado], height=600, scrolling=True)
    



