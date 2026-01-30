import csv
import sqlite3
from pathlib import Path


csv_path = Path('data/produtos.csv')  
db_path = Path('produtos.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id_produto TEXT PRIMARY KEY,
    nome_produto TEXT NOT NULL,
    categoria TEXT,
    marca TEXT,
    preco_atual REAL,
    data_criacao TEXT
)
''')

with open(csv_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''
        INSERT OR REPLACE INTO produtos 
        (id_produto, nome_produto, categoria, marca, preco_atual, data_criacao)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            row['id_produto'],
            row['nome_produto'],
            row['categoria'],
            row['marca'],
            float(row['preco_atual']),
            row['data_criacao']
        ))

conn.commit()
conn.close()
print(f"Dados importados com sucesso! Total: {cursor.rowcount} registros.")