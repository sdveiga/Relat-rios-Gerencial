import streamlit as st
import pandas as pd
from PIL import Image

# Simulação de login
def login():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")
    role = st.sidebar.selectbox("Nível Hierárquico", ["CEO", "DIRETOR", "GERENTE", "COORDENADOR", "SUPERVISOR", "OPERADOR", "TECNICO"])
    setor = st.sidebar.radio("Setor de Atuação", ["Instalação", "Manutenção"])
    if st.sidebar.button("Entrar"):
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = role
        st.session_state.setor = setor

# Lista de todos os indicadores
todos = [
    "CERTIFICADO", "TEC1", "HIERARQUIA", "IQI", "OS DIGITAL", "EFICIENCIA", "BLINDAGEM TV",
    "CUSTO DE MATERIAL", "LOG VT", "QUEBRA", "VT POR EQUIPE", "ROTA INICIAL", "ROTA FINAL",
    "FATURAMENTO GERAL", "PONTUAÇÃO INSTALAÇÃO", "DESCONTO DE REVISTA", "PRODUTIVIDADE ONLINE"
]

# Indicadores por cargo
def indicadores_por_cargo(cargo):
    indicadores = {
        "CEO": todos,
        "DIRETOR": todos,
        "GERENTE": todos,
        "COORDENADOR": todos,
        "SUPERVISOR": todos_menos(["FATURAMENTO GERAL", "PONTUAÇÃO INSTALAÇÃO", "DESCONTO DE REVISTA", "PRODUTIVIDADE ONLINE"]),
        "OPERADOR": todos_menos(["VT POR EQUIPE", "ROTA INICIAL", "ROTA FINAL", "FATURAMENTO GERAL", "PONTUAÇÃO INSTALAÇÃO", "DESCONTO DE REVISTA", "PRODUTIVIDADE ONLINE"]),
        "TECNICO": todos_menos(["VT POR EQUIPE", "ROTA INICIAL", "ROTA FINAL", "FATURAMENTO GERAL", "PONTUAÇÃO INSTALAÇÃO", "DESCONTO DE REVISTA", "PRODUTIVIDADE ONLINE"]),
    }
    return indicadores.get(cargo, [])

def todos_menos(lista):
    return [i for i in todos if i not in lista]

# Metas por setor
metas_instalacao = {
    "1º Trabalho": 90, "Aderência na URA": 95, "Baixa TOA": 90, "Baixa TMO": 95,
    "Comunicação Com Padrão": 90, "Inspeções Conformes": 85, "Produtividade": 90,
    "NR 35": 95, "O.S Digital": 25, "Qualidade Atendimento": 90, "Quebra Qualificada": 90,
    "Quebra": 5, "TEC1": 90, "Tempo em atendimento": 25, "Tempo em deslocamento": 25,
    "Técnico Consultivo": 25, "Recomendação MESH": 90, "BDS": 90, "Certidão Atendimento": 90,
    "Qualidade Atendimento com Falha": 90, "% Avaliação": 75, "TNPS Jornada": 75
}

metas_manutencao = metas_instalacao.copy()
metas_manutencao.update({
    "Tempo em atendimento": 15,
    "Tempo em deslocamento": 15,
    "Técnico Consultivo": 15,
    "Certidão Atendimento": None  # Não aplicável
})

# Página principal
def main():
    st.title("📊 Painel de Indicadores")
    st.sidebar.image("foto_usuario.jpg", width=150)
    st.sidebar.markdown(f"👋 Seja bem-vindo, **{st.session_state.username}**")
    st.sidebar.markdown("### Menu")
    page = st.sidebar.radio("Navegação", ["Indicadores", "Justificativas", "IVM"])

    if page == "Indicadores":
        st.subheader("🔍 Indicadores disponíveis")
        indicadores = indicadores_por_cargo(st.session_state.role)
        for indicador in indicadores:
            st.markdown(f"- {indicador}")
        st.markdown("### 📈 Visualização Power BI")
        st.components.v1.iframe("https://app.powerbi.com/view?r=SEU_LINK_AQUI", height=600, scrolling=True)

        st.markdown("### 🎯 Metas do Setor")
        metas = metas_instalacao if st.session_state.setor == "Instalação" else metas_manutencao
        df_metas = pd.DataFrame(list(metas.items()), columns=["Indicador", "Meta"])
        st.dataframe(df_metas)

    elif page == "Justificativas":
        st.subheader("📝 Justificativa de Resultados")
        indicador = st.selectbox("Indicador", todos)
        fato = st.text_area("Fato")
        causa = st.text_area("Causa")
        acao = st.text_area("Ação")
        if st.button("Enviar Justificativa"):
            nova_justificativa = {
                "Usuário": st.session_state.username,
                "Indicador": indicador,
                "Fato": fato,
                "Causa": causa,
                "Ação": acao
            }
            if "justificativas" not in st.session_state:
                st.session_state.justificativas = []
            st.session_state.justificativas.append(nova_justificativa)
            st.success("Justificativa registrada com sucesso!")

        if "justificativas" in st.session_state:
            st.markdown("### 📋 Histórico de Justificativas")
            df = pd.DataFrame(st.session_state.justificativas)
            st.dataframe(df)

    elif page == "IVM":
        st.subheader("📋 Formulário IVM")
        st.markdown("Preencha o formulário abaixo:")
        st.components.v1.iframe("https://forms.office.com/YOUR_FORM_LINK", height=700)

# Inicialização
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    main()
