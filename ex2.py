from pathlib import Path

# Define o diretório raiz onde estão os arquivos
root_dir = Path('files')

# iterdir() cria um iterador com todos os itens da pasta (arquivos e diretórios)
file_paths = root_dir.iterdir()

# Mostra o diretório atual onde o script está sendo executado
# Muito útil pra debug (evita confusão com caminhos relativos)
print(Path.cwd())

# Percorre cada item dentro da pasta
for path in file_paths:

    # Cria um novo nome para o arquivo:
    # path.stem → nome sem extensão
    # path.suffix → extensão (.txt, .csv, etc)
    # Ex: abc.txt → new_abc.txt
    new_filename = 'new_' + path.stem + path.suffix

    # Cria um novo caminho (Path) com o nome atualizado
    # Não altera o arquivo ainda, só prepara o novo caminho
    new_filepath = path.with_name(new_filename)

    # Mostra o novo caminho gerado
    print(new_filepath)

    # Renomeia o arquivo (ou move, se o caminho for diferente)
    path.rename(new_filepath)