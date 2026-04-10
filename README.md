O que é o Pathlib?

pathlib é uma biblioteca padrão do Python para trabalhar com caminhos de forma orientada a objetos.

Ela substitui o os.path, deixando o código:

Mais legível
Mais seguro
Mais portátil

Por que usar?

Manipulação de arquivos é comum em vários cenários:

Organização de diretórios
Processamento de dados
Gerenciamento de arquivos
Compactação e extração
Limpeza de arquivos

O pathlib simplifica tudo isso com uma API clara e poderosa.

Exemplos

Cada arquivo aborda um conceito específico:

ex01 — Introdução ao Path (criação, propriedades, navegação)
ex02 — Renomeação de arquivos
ex03 — Renomeação baseada na pasta
ex04 — Nome baseado na hierarquia
ex05 — Renomeação com data (timestamp)
ex06 — Alteração de extensão
ex07 — Criação de arquivos em lote
ex08 — Compactação (.zip)
ex09 — Extração de ZIP
ex10 — Busca de arquivos
ex11 — Limpeza de arquivos

Boas práticas

Verifique se é arquivo (is_file())
Evite sobrescrever sem necessidade
Cuidado com operações destrutivas (unlink())
Valide arquivos ao extrair ZIP
Evite caracteres inválidos em nomes

Progressão do projeto

Fundamentos
Navegação
Manipulação de nomes
Automação
Casos reais (ZIP, busca, limpeza)

Próximos passos

Criar uma CLI
Organizar downloads automaticamente
Implementar backup
Montar pipeline de arquivos

Conclusão

Aprender pathlib é essencial para trabalhar com automação e arquivos em Python.
