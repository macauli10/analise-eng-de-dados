# executando sql
import duckdb
import sys

def executar_queries_sql():
    conn = duckdb.connect('preco_competidores.db')
    if len(sys.argv) < 2:
        print("teste")
        print("executando")
        query = "SELECT * FROM precos_competidores LIMIT 5"
        df = conn.execute(query).df()
        print(df)
        conn.close()
        return
    
    arquivo_sql = sys.argv[1]
    
    try:
        with open(arquivo_sql, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        queries = [q.strip() for q in conteudo.split(';') if q.strip()]

        for i, query in enumerate(queries, 1):
            print(f"\n{'═'*60}")
            print(f"📋 QUERY {i}")
            print(f"{'═'*60}")
            print(f"{query}\n")
            print(f"{'─'*60}")
            
            try:
                df = conn.execute(query).df()
                if not df.empty:
                    print(f"resultados ({len(df)} linhas):")
                    print(df.to_string(index=False))
                else:
                    print("query executada")
                    
            except Exception as e:
                print(f"erro {i}: {e}")
    
    except FileNotFoundError:
        print(f"arquivo não encontrado {arquivo_sql}")
    except Exception as e:
        print(f"erro de processo {e}")
    
    finally:
        conn.close()

if __name__ == "__main__":
    executar_queries_sql()