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

        if aba_fca == "🔧 Preenchimento FCA":

        # Parte 3 e Parte 4 entram aqui

    elif menu == "🔒 Sair":
        st.session_state.logado = False
        st.experimental_rerun()
                if aba_fca == "🔧 Preenchimento FCA":
                    
        indicadores_bom_para_baixo = [
            "1º Trabalho", "Quebra de Agenda", "Quebra Qualificada", "Revisita",
            "Certidão Validado Com falha", "Serviço não realizado", "Serviço realizado, sem Resolução"
        ]

        def esta_fora_da_meta(item):
            if item["Indicador"] in indicadores_bom_para_baixo:
                return float(item["Nota Atual"]) > float(item["Meta"])
            else:
                return float(item["Nota Atual"]) < float(item["Meta"])

        if not os.path.exists(caminho_csv):
            colunas = ["Indicador", "Fato", "Causas", "Ações", "Mês", "Supervisor", "Cargo Supervisor", "Tipo", "Nota Atual", "Meta", "Evidencias"]
            pd.DataFrame(columns=colunas).to_csv(caminho_csv, index=False)

        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        indicadores = [
            {"Indicador": "1º Trabalho", "Instalacao": 20, "Manutencao": 30},
            {"Indicador": "Aderência na URA", "Instalacao": 90, "Manutencao": 90},
            {"Indicador": "Baixa TOA", "Instalacao": 95, "Manutencao": 95},
            {"Indicador": "Com Geolocalização", "Instalacao": 90, "Manutencao": 90},
            {"Indicador": "Geolocalização Com Padrão", "Instalacao": 90, "Manutencao": 90},
            {"Indicador": "Inspeções Conformes", "Instalacao": 85, "Manutencao": None},
            {"Indicador": "Inspeções Realizadas", "Instalacao": 35, "Manutencao": None},
            {"Indicador": "NR 35", "Instalacao": 99, "Manutencao": None},
            {"Indicador": "O.S Digital", "Instalacao": 98, "Manutencao": None},
            {"Indicador": "Produtividade", "Instalacao": 2.5, "Manutencao": 6},
            {"Indicador": "Quebra de Agenda", "Instalacao": 25, "Manutencao": 15},
            {"Indicador": "Quebra Qualificada", "Instalacao": 7, "Manutencao": 6},
            {"Indicador": "Revisita", "Instalacao": 7, "Manutencao": 7},
            {"Indicador": "TEC1", "Instalacao": 96, "Manutencao": 97},
            {"Indicador": "Técnico Consultivo", "Instalacao": 2.5, "Manutencao": 2.5},
            {"Indicador": "Recomendação MESH", "Instalacao": None, "Manutencao": 90},
            {"Indicador": "Bandsteering", "Instalacao": 90, "Manutencao": None},
            {"Indicador": "Certidão Atendimento", "Instalacao": 90, "Manutencao": 90},
            {"Indicador": "Certidão Validado Com falha", "Instalacao": 20, "Manutencao": 20},
            {"Indicador": "%Blindagem", "Instalacao": None, "Manutencao": 90},
            {"Indicador": "% Avaliação", "Instalacao": 15, "Manutencao": 15},
            {"Indicador": "TNPS Jornada", "Instalacao": 75, "Manutencao": 75},
            {"Indicador": "Serviço não realizado", "Instalacao": 0.3, "Manutencao": 0.3},
            {"Indicador": "Serviço realizado, sem Resolução", "Instalacao": 7, "Manutencao": 7}
        ]
        df_base = pd.DataFrame(indicadores)

        st.title("📋 Preenchimento FCA dos Indicadores")
        mes_ref = st.selectbox("📅 Mês de referência", meses)
        tipo = st.selectbox("🔧 Tipo de operação", ["Instalação", "Manutenção"])
        coluna_meta = "Instalacao" if tipo == "Instalação" else "Manutencao"

        df_filtrado = df_base[df_base[coluna_meta].notnull()].copy()
        notas = []
        metas = []

        for i, row in df_filtrado.iterrows():
            meta = row[coluna_meta]
            nota = st.number_input(f"{row['Indicador']} (Meta: {meta})", min_value=0.0, value=0.0, step=0.1, key=f"nota_{i}")
            notas.append(nota)
            metas.append(meta)

        df_filtrado["Meta"] = metas
        df_filtrado["Nota Atual"] = notas
        df_filtrado["Status"] = df_filtrado.apply(
            lambda row: "Dentro da Meta" if not esta_fora_da_meta(row) else "Fora da Meta",
            axis=1
        )
        st.dataframe(df_filtrado[["Indicador", "Meta", "Nota Atual", "Status"]])

        st.subheader("🧠 FCA - Fato, Causa, Ação + Evidências")
        fca_data = []

        for i, row in df_filtrado.iterrows():
            if row["Status"] == "Fora da Meta":
                st.markdown(f"### {row['Indicador']}")
                fato = st.text_area(f"Fato ({row['Indicador']})", key=f"fato_{i}")
                causas = st.text_area(f"Causas separadas por vírgula ({row['Indicador']})", key=f"causa_{i}")
                acoes = st.text_area(f"Ações separadas por vírgula ({row['Indicador']})", key=f"acao_{i}")
                evid1 = st.file_uploader(f"Evidência 1 - {row['Indicador']}", type=["png", "jpg", "jpeg"], key=f"evid1_{i}")
                evid2 = st.file_uploader(f"Evidência 2 - {row['Indicador']}", type=["png", "jpg", "jpeg"], key=f"evid2_{i}")

                fca_data.append({
                    "Indicador": row["Indicador"],
                    "Fato": fato,
                    "Causas": [c.strip() for c in causas.split(",") if c.strip()],
                    "Ações": [a.strip() for a in acoes.split(",") if a.strip()],
                    "Evidencias": [evid1, evid2],
                    "Mês": mes_ref,
                    "Supervisor": nome,
                    "Cargo Supervisor": cargo,
                    "Tipo": tipo,
                    "Nota Atual": row["Nota Atual"],
                    "Meta": row["Meta"]
                })

        if st.button("Salvar FCA"):
            df_novo = pd.DataFrame(fca_data).drop(columns=["Evidencias"], errors="ignore")
            df_existente = pd.read_csv(caminho_csv)
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
            df_final.to_csv(caminho_csv, index=False)
            st.success("✅ FCA salvo com sucesso!")
        st.title("🎯 Apresentação dos Indicadores e FCA")

        if st.button("🗑️ Apagar todos os registros anteriores"):
            os.remove(caminho_csv)
            pd.DataFrame(columns=["Indicador", "Fato", "Causas", "Ações", "Mês", "Supervisor", "Cargo Supervisor", "Tipo", "Nota Atual", "Meta", "Evidencias"]).to_csv(caminho_csv, index=False)
            st.success("Todos os registros foram apagados.")

        historico_df = pd.read_csv(caminho_csv)
        historico = historico_df.to_dict(orient="records")

        mes_selecionado = st.selectbox("📅 Selecione o mês", meses)
        tipo_filtro = st.selectbox("🔧 Tipo de operação", ["Instalação", "Manutenção"])
        supervisor_filtro = st.text_input("🔍 Filtrar por nome do responsável (opcional)")

        dados_filtrados = [
            item for item in historico
            if item["Mês"] == mes_selecionado
            and item["Tipo"] == tipo_filtro
            and pode_ver(cargo, item.get("Cargo Supervisor", ""))
            and (supervisor_filtro.lower() in item["Supervisor"].lower() if supervisor_filtro else True)
            and esta_fora_da_meta(item)
        ]

        if not dados_filtrados:
            st.info("Nenhum indicador fora da meta para os filtros selecionados.")
        else:
            for idx, item in enumerate(dados_filtrados):
                st.markdown(f"### {item['Indicador']}")
                col1, col2, col3, col4 = st.columns(4)
                col1.markdown(f"**Fato:** {item['Fato']}")
                col2.markdown(f"**Causa:** {', '.join(item['Causas'])}")
                col3.markdown(f"**Ação:** {', '.join(item['Ações'])}")
                col4.markdown(f"**Meta:** {item['Meta']}<br>**Nota:** {item['Nota Atual']}", unsafe_allow_html=True)

                # Pareto de Causas
                causas = item.get("Causas", [])
                if isinstance(causas, list) and causas:
                    causas_df = pd.DataFrame({"Causa": causas})
                    causas_df["Contagem"] = 1
                    causas_agg = causas_df.groupby("Causa").count().reset_index().sort_values("Contagem", ascending=False)
                    fig_causa = px.bar(causas_agg, x="Causa", y="Contagem", title="Pareto de Causas")
                    st.plotly_chart(fig_causa, use_container_width=True, key=f"causa_{idx}")

                # Pareto de Ações
                acoes = item.get("Ações", [])
                if isinstance(acoes, list) and acoes:
                    acoes_df = pd.DataFrame({"Ação": acoes})
                    acoes_df["Contagem"] = 1
                    acoes_agg = acoes_df.groupby("Ação").count().reset_index().sort_values("Contagem", ascending=False)
                    fig_acao = px.bar(acoes_agg, x="Ação", y="Contagem", title="Pareto de Ações")
                    st.plotly_chart(fig_acao, use_container_width=True, key=f"acao_{idx}")

                st.markdown("📸 **EVIDÊNCIA (FOTO 1)**")
                st.markdown("📸 **EVIDÊNCIA (FOTO 2)**")
                st.markdown("---")

            # Exportar CSV
            df_export = pd.DataFrame(dados_filtrados).drop(columns=["Evidencias"], errors="ignore")
            csv = df_export.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Baixar FCA em CSV", data=csv, file_name=f"fca_{mes_selecionado}_{tipo_filtro}.csv", mime="text/csv")
