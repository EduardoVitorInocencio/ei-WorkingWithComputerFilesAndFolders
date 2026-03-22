from pathlib import Path

# Define o diretório raiz onde os arquivos estão localizados
root_dir = Path('files')

# Percorre todos os arquivos .txt dentro da pasta e subpastas (recursivamente)
for path in root_dir.glob('**/*.txt'):

    # Garante que estamos lidando apenas com arquivos (boa prática)
    if path.is_file():

        # path.parts → retorna uma tupla com todas as partes do caminho
        # Ex: ('files', 'pasta1', 'pasta2', 'arquivo.txt')
        path_parts = path.parts

        # Seleciona apenas as subpastas (exclui o root 'files' e o nome do arquivo)
        # [1:-1] → começa da primeira subpasta até antes do arquivo
        # Ex: ('pasta1', 'pasta2')
        subfolders = path_parts[1:-1]

        # Cria um novo nome de arquivo baseado nas subpastas
        # Junta tudo com "_" e adiciona o nome original
        # Ex: pasta1_pasta2_arquivo.txt
        new_filename = '_'.join(subfolders) + '_' + path.name

        # Cria um novo caminho com o nome atualizado (sem mover de pasta)
        new_filepath = path.with_name(new_filename)

        # Renomeia o arquivo
        path.rename(new_filepath)