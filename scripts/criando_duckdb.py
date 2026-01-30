# criando banco duckdb
import duckdb

conn = duckdb.connect('preco_competidores.db')
conn.execute("""
    CREATE OR REPLACE TABLE precos_competidores AS 
    SELECT *
    FROM 'data/preco_competidores.parquet'
""")
print(f"funcionou")
conn.close()