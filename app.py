import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# 1. Configurações Iniciais e Banco de Dados
st.set_page_config(page_title="Dashboard Acadêmico", layout="wide", page_icon="🎓")

# Substitua pela sua Connection String real
string_conexao = st.secrets["DB_URL"]

@st.cache_resource
def inicializar_conexao():
    return create_engine(string_conexao)

engine = inicializar_conexao()

# 2. Criando o Menu Lateral (Sidebar)
st.sidebar.title("Navegação 🧭")
st.sidebar.markdown("Selecione a análise que deseja visualizar:")

# O selectbox cria um menu suspenso elegante
opcao_selecionada = st.sidebar.selectbox(
    "Escolha uma métrica:",
    [
        "1. Horas de Estudo Diárias",
        "2. Engajamento em Projetos/Estágios",
        "3. Nível de Estresse",
        "4. Horas de Sono",
        "5. Tempo de Tela (Lazer)",
        "6. Consistência nos Estudos"
    ]
)

# 3. Dicionário de Configuração (O cérebro do nosso código DRY)
# Mapeamos o que o usuário escolheu no menu para a coluna real do banco e o título do gráfico
config_analises = {
    "1. Horas de Estudo Diárias": {"coluna": "study_hours_daily", "titulo": "Impacto das Horas de Estudo nas Notas"},
    "2. Engajamento em Projetos/Estágios": {"coluna": "projects_internships", "titulo": "O Peso da Prática (Projetos/Estágios)"},
    "3. Nível de Estresse": {"coluna": "stress_level", "titulo": "Desempenho por Nível de Estresse"},
    "4. Horas de Sono": {"coluna": "sleep_hours", "titulo": "Relação entre Horas de Sono e Notas"},
    "5. Tempo de Tela (Lazer)": {"coluna": "screen_time_non_study", "titulo": "Impacto do Tempo de Tela Fora dos Estudos"},
    "6. Consistência nos Estudos": {"coluna": "study_consistency", "titulo": "O Poder da Consistência Acadêmica"}
}

# 4. A Função Principal (Busca os dados e desenha a tela)
def gerar_analise(coluna_x, titulo_grafico):
    st.title("🎓 Raio-X do Desempenho Acadêmico")
    st.markdown("---")
    st.subheader(titulo_grafico)
    
    # Query SQL Dinâmica: Injeta a coluna escolhida direto no SELECT e no GROUP BY
    query = f"""
    SELECT
        {coluna_x},
        cgpa_category,
        COUNT(*) as quantidade
    FROM estudantes_notas
    GROUP BY {coluna_x}, cgpa_category
    ORDER BY {coluna_x}, cgpa_category;
    """
    
    # Executa a query
    df_resultado = pd.read_sql(query, con=engine)
    
    # Divide a tela em duas colunas (Tabela à esquerda, Gráfico à direita)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**Resumo dos Dados (PostgreSQL):**")
        st.dataframe(df_resultado, use_container_width=True)
        
    with col2:
        fig = px.bar(
            df_resultado,
            x=coluna_x,
            y="quantidade",
            color="cgpa_category",
            barmode="group",
            title=titulo_grafico,
            text_auto=True
        )
        st.plotly_chart(fig, use_container_width=True)

# 5. Executando a mágica
# Pegamos as configurações baseadas na escolha do usuário e passamos para a função
coluna_alvo = config_analises[opcao_selecionada]["coluna"]
titulo_alvo = config_analises[opcao_selecionada]["titulo"]

gerar_analise(coluna_alvo, titulo_alvo)

# Mensagem de rodapé no menu lateral
st.sidebar.markdown("---")
st.sidebar.info("Dashboard construído com Streamlit, Plotly e PostgreSQL.")