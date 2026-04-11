from pathlib import Path

# Define o diretório raiz como o diretório atual (onde o script está rodando)
root_dir = Path('.')

# Termo que será buscado no nome dos arquivos
search_term = 'archive'

# rglob('*') percorre TODOS os arquivos e pastas recursivamente
for path in root_dir.rglob('*'):

    # Garante que estamos lidando apenas com arquivos
    if path.is_file():

        # Verifica se o termo de busca está no nome do arquivo (sem extensão)
        # path.stem → nome do arquivo sem extensão
        if search_term in path.stem:

            # Mostra o caminho absoluto do arquivo encontrado
            # absolute() → caminho completo no sistema
            print(path.absolute())