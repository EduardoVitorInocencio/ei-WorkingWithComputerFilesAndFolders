from pathlib import Path
import zipfile

# Diretório onde estão os arquivos .zip
root_dir = Path('files')

# Diretório de destino onde os arquivos serão extraídos
destination_path = Path('destination')

# Percorre todos os arquivos .zip dentro da pasta (não recursivo)
for path in root_dir.glob('*.zip'):

    # Abre o arquivo zip no modo leitura ('r')
    with zipfile.ZipFile(path, 'r') as zf:

        # Cria um diretório com o nome do arquivo zip (sem extensão)
        # Ex: archive.zip → destination/archive/
        final_path = destination_path / Path(path.stem)

        # Extrai TODO o conteúdo do zip para esse diretório
        zf.extractall(path=final_path)