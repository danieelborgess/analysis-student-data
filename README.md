# 🎓 Raio-X do Desempenho Acadêmico

> Projeto de Engenharia e Análise de Dados utilizando **Python, PostgreSQL, SQL e Streamlit** para identificar fatores associados ao desempenho acadêmico.

## 📖 Sobre o Projeto

Este projeto implementa um pipeline completo de análise de dados, desde a limpeza e transformação dos dados até a construção de um dashboard interativo conectado a um banco de dados relacional na nuvem.

O objetivo é responder perguntas de negócio sobre hábitos de estudo e desempenho acadêmico utilizando uma arquitetura próxima da encontrada em projetos reais de análise de dados.

---

## 🛠️ Tecnologias Utilizadas

* **Python (Pandas):** Limpeza, tratamento e Análise Exploratória de Dados (EDA).
* **PostgreSQL (Neon DB):** Banco de dados relacional hospedado na nuvem.
* **SQLAlchemy & Psycopg2:** Comunicação entre a aplicação Python e o banco PostgreSQL.
* **SQL:** Consultas analíticas para obtenção dos dados utilizados pelo dashboard.
* **Streamlit:** Desenvolvimento da aplicação web interativa.
* **Plotly:** Construção dos gráficos interativos.

---

## 🏗️ Arquitetura do Projeto

```text
Dataset (CSV)
        │
        ▼
Python + Pandas
(Limpeza e EDA)
        │
        ▼
PostgreSQL (Neon)
        │
        ▼
Consultas SQL
        │
        ▼
Streamlit
        │
        ▼
Dashboard Interativo
```

---

## 📊 Pipeline de Desenvolvimento

### 🔹 Fase 1 — Limpeza e Análise Exploratória

Toda a preparação dos dados foi realizada no Google Colab (`data_student.ipynb`), incluindo:

* tratamento de valores nulos;
* conversão de tipos de dados;
* padronização das colunas;
* criação de novas variáveis;
* análise exploratória (EDA);
* geração de gráficos para responder perguntas de negócio.

Foram respondidas seis perguntas principais sobre os fatores associados ao desempenho acadêmico.

---

### 🔹 Fase 2 — Engenharia de Dados

Após o tratamento dos dados, o dataframe foi migrado para um banco PostgreSQL hospedado no **Neon**.

Essa etapa permitiu criar uma única fonte de dados (Single Source of Truth), separando o processamento dos dados da aplicação responsável pela visualização.

---

### 🔹 Fase 3 — Dashboard

O dashboard foi desenvolvido utilizando **Streamlit**.

Em vez de processar novamente o dataset com Pandas, a aplicação realiza consultas SQL diretamente no banco PostgreSQL e utiliza apenas os resultados para gerar os gráficos.

Essa abordagem reduz o processamento realizado pela aplicação e aproxima o projeto de uma arquitetura utilizada em aplicações analíticas.

---

## 🗄️ Exemplo de Consulta SQL

Uma das consultas utilizadas durante o desenvolvimento foi:

```sql
SELECT
    stress_level,
    cgpa_category,
    COUNT(*) AS quantidade
FROM estudantes_notas
GROUP BY
    stress_level,
    cgpa_category
ORDER BY
    stress_level,
    cgpa_category;
```

---

## 💡 Principais Descobertas

* **Consistência supera intensidade:** estudantes com uma rotina de estudos mais consistente apresentaram maior frequência de notas elevadas.

* **Estresse e desempenho:** neste conjunto de dados, estudantes com níveis mais altos de estresse também apresentaram maior frequência de notas altas, indicando uma associação que merece investigação mais aprofundada, mas que não implica relação de causa e efeito.

* **Sono equilibrado:** a faixa entre 6 e 7 horas de sono concentrou a maior quantidade de estudantes com melhor desempenho acadêmico.

---

## ✅ Competências Demonstradas

Durante o desenvolvimento deste projeto foram aplicadas as seguintes competências:

* Limpeza e transformação de dados com Pandas;
* Análise Exploratória de Dados (EDA);
* Manipulação de DataFrames;
* Construção de consultas SQL;
* Integração Python ↔ PostgreSQL;
* Persistência de dados em banco relacional;
* Desenvolvimento de dashboard interativo;
* Visualização de dados com Plotly;
* Deploy de aplicação utilizando Streamlit Cloud.

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/danieelborgess/analysis-student-data.git
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as credenciais do banco

Crie uma pasta chamada `.streamlit` na raiz do projeto e, dentro dela, um arquivo chamado `secrets.toml`.

Adicione sua string de conexão:

```toml
DB_URL = "postgresql://usuario:senha@host/banco"
```

### 4. Execute o dashboard

```bash
streamlit run app.py
```

---

## 🎯 Objetivos do Projeto

Este projeto foi desenvolvido com o objetivo de praticar e demonstrar conhecimentos em:

* Engenharia de Dados;
* Análise Exploratória de Dados;
* SQL e PostgreSQL;
* Integração entre Python e bancos relacionais;
* Desenvolvimento de dashboards interativos;
* Construção de um pipeline de dados ponta a ponta.

---

## 📂 Estrutura do Repositório

```text
├── data_student.ipynb      # Limpeza, tratamento e EDA
├── app.py                  # Dashboard em Streamlit
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml
```
