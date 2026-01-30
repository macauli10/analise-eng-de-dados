# 📊 Análise-Eng-de-Dados 

Projeto de análise exploratória para prática de engenharia de dados.

## 🎯 Objetivo
Criar um pipeline simples para processar dados de diferentes fontes e formatos.

## 🗂️ Estrutura

```
data/                       # Arquivos de dados
├── clientes.csv            # Dados de clientes
├── produtos.csv            # Catálogo de produtos
├── vendas.csv              # Registro de vendas
└── preco_competidores.parquet  # Preços concorrentes (Parquet)

tratamento/                 # Notebooks de análise
└── limpeza.ipynb           # Análise exploratória

scripts/                    # Scripts Python
├── connect.py              # Conexão com Supabase S3
├── criando_duckdb.py       # Criação do DuckDB
├── import.py               # Importação de dados
└── executar_sql.py         # Execução de queries

bancos/                     # Bancos de dados locais
├── produtos.db             # SQLite com dados CSV
└── preco_competidores.db   # DuckDB com dados Parquet

queries.sql                 # Consultas SQL para análise
```

## 🔧 Funcionalidades

1. **Conexão com Supabase S3**
   - Acesso a data lake cloud
   - Download de arquivos Parquet

2. **Processamento Multi-formato**
   - CSV → SQLite (dados estruturados)
   - Parquet → DuckDB (dados otimizados)

3. **Análise Exploratória**
   - Notebook Jupyter para limpeza
   - Análise com Pandas
   - Queries SQL para insights

## 🚀 Como Usar

### 1. Processar dados Parquet (Supabase)
```bash
python connect.py
python criando_duckdb.py
```

### 2. Importar dados CSV para SQLite
```bash
python import.py
```

### 3. Executar análises
```bash
# Abra o notebook
jupyter notebook tratamento/limpeza.ipynb

# Ou execute queries SQL
python executar_sql.py
```

## 🛠️ Tecnologias
- **Python** (Pandas, DuckDB, sqlite3)
- **Supabase S3** - Data Lake
- **DuckDB** - Análise de dados Parquet
- **SQLite** - Dados relacionais
- **Jupyter Notebook** - Análise interativa

## 📊 Fontes de Dados
Baseado no material da **"Jornada de Dados - Luciano"**:
- Dados simulados de e-commerce
- Preços de concorrentes
- Catálogo de produtos
- Histórico de vendas

## 🎓 Aprendizados
- Trabalhar com diferentes formatos (CSV, Parquet)
- Conexão com serviços cloud (Supabase)
- Uso de bancos embutidos (DuckDB, SQLite)
- Análise exploratória com Pandas

---
