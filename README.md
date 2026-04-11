Manipulação de Arquivos com Pathlib (Python)
Coleção de exemplos práticos usando a biblioteca padrão pathlib para manipular arquivos e diretórios de forma segura e legível.

Sumário

Sobre
Recursos mostrados
Estrutura do repositório
Como usar (Quick start)
Exemplos rápidos
Boas práticas
Possíveis evoluções
Autor
Sobre
O objetivo é ensinar, através de pequenos scripts, tarefas reais de automação envolvendo caminhos, renomeação, compactação, busca e limpeza de arquivos. Os exemplos evoluem do básico ao prático.

Recursos mostrados

Criação e manipulação de caminhos (Path)
Verificação de existência e tipo (exists, is_file, is_dir)
Iteração e busca (iterdir, glob, rglob)
Propriedades e transformação de nomes (name, stem, suffix, with_suffix)
Renomeação e movimentação (rename, replace)
Criação de arquivos (touch) e diretórios (mkdir, exist_ok)
Operações com metadata (stat, timestamps)
Compactação e extração (zipfile)
Remoção segura (unlink)
Tratamento de edge cases (caracteres inválidos, sobrescrita)
Estrutura do repositório

ex01.py — Introdução ao Pathlib (criar Path, propriedades, iterdir)
ex02.py — Renomeação simples em lote
ex03.py — Renomeação com base na pasta pai (glob recursivo)
ex04.py — Nomes baseados na hierarquia de pastas
ex05.py — Renomeação com timestamp (stat + datetime)
ex06.py — Alteração de extensões (with_suffix)
ex07.py — Criação de múltiplos arquivos (touch)
ex08.py — Compactação em ZIP (zipfile)
ex09.py — Extração de ZIP (extractall com validação)
ex10.py — Busca avançada (rglob + filtros)
ex11.py — Limpeza automatizada (unlink com checagens)
Quick start

Clone o repositório: git clone
Entre na pasta: cd
Execute um exemplo: python ex01.py
Exemplos rápidos (trechos)

Criar e checar um Path
from pathlib import Path
p = Path('docs/report.txt')
if p.exists() and p.is_file():
print(p.name, p.suffix)

Renomear arquivos .txt para .md (seguro)
for f in Path('notes').rglob('*.txt'):
new = f.with_suffix('.md')
if not new.exists():
    f.rename(new)

Compactar arquivos selecionados
import zipfile
from pathlib import Path
files = list(Path('data').rglob('*.csv'))
with zipfile.ZipFile('backup.zip', 'w') as z:
for f in files:
    z.write(f, arcname=f.relative_to('data'))

Boas práticas

Sempre verificar is_file() antes de operar
Evitar sobrescrita: checar existence antes de rename() ou write
Fazer backups antes de operações destrutivas
Validar / sanitizar nomes ao manipular uploads ou extração de ZIP
Tratar diferenças de path entre OS (use Path / PurePath)
Sugestões de evolução

CLI com argparse ou click para rodar cada exNN com flags
Organizador automático de pasta Downloads
Ferramenta de backup incremental (hash + zip)
Pipeline ETL simples usando pathlib + pandas
Testes unitários para cada exemplo
Licença
Código aberto — adapte conforme necessário (ex.: MIT).

Autor
Projeto para estudo e revisão sobre manipulação de arquivos com Python.