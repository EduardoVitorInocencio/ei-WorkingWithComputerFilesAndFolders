from pathlib import Path

# Define o diretório raiz onde os arquivos estão localizados
root_dir = Path('files')

# Percorre todos os arquivos .txt dentro da pasta e subpastas (recursivamente)
for path in root_dir.glob('**/*.txt'):

    # Garante que estamos lidando apenas com arquivos (evita erro com diretórios)
    if path.is_file():

        # Cria um novo caminho alterando apenas a extensão do arquivo
        # Ex: arquivo.txt → arquivo.csv
        # ⚠️ Não altera o conteúdo, apenas o nome/extensão
        new_filepath = path.with_suffix('.csv')

        # Renomeia o arquivo (na prática, troca a extensão)
        path.rename(new_filepath)