# Importar biblioteca para trabalhar dentro do diretório
import os 

# Entrando dentro do diretório
diretorio = r"C:/Users/vinicius.oliveira/Desktop/Teste/"

# Percorrendo o diretório
result = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
print(result)

# Importando biblioteca de transformação de dados
import pandas as pd

# Importando bliblioteca para trabalhar com arquivos parquet
import pyarrow

# Tranformando os arquivos\s
for arquivo in result:
    df = pd.read_parquet(diretorio + arquivo)
    csv_out = r'C:/Users/vinicius.oliveira/Desktop/Teste/'+ arquivo[:-8] + '.csv'
    output = df.to_csv(csv_out, sep=';', index = False)

