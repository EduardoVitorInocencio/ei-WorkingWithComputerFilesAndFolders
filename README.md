============================================================
       MANIPULAÇÃO DE ARQUIVOS COM PATHLIB (PYTHON)
============================================================

Este repositório contém exemplos práticos de como utilizar a 
biblioteca 'pathlib' para automatizar tarefas de diretórios 
e arquivos de forma moderna e orientada a objetos.

------------------------------------------------------------
1. POR QUE PATHLIB?
------------------------------------------------------------
* Substitui o antigo 'os.path'.
* Código mais legível e intuitivo.
* Compatível com Windows, Linux e macOS (Portável).
* API poderosa para automação e ETL.

------------------------------------------------------------
2. RESUMO DOS EXEMPLOS (exXX.py)
------------------------------------------------------------

[ FUNDAMENTOS ]
ex01.py: Introdução, verificação de existência e propriedades.
ex07.py: Criação de múltiplos arquivos em lote (touch).

[ RENOMEAÇÃO E ORGANIZAÇÃO ]
ex02.py: Renomeação simples de arquivos.
ex03.py: Renomeação baseada na pasta pai.
ex04.py: Renomeação baseada na hierarquia de subpastas.
ex05.py: Uso de Timestamps (datas) nos nomes.
ex06.py: Alteração de extensões (ex: .txt para .csv).

[ OPERAÇÕES AVANÇADAS ]
ex08.py: Compactação de arquivos (ZIP).
ex09.py: Extração de arquivos ZIP e organização.
ex10.py: Busca recursiva avançada (rglob).
ex11.py: Limpeza e remoção de arquivos (unlink).

------------------------------------------------------------
3. BOAS PRÁTICAS
------------------------------------------------------------
- Use .is_file() antes de manipular arquivos.
- Use .with_suffix() para trocar extensões com segurança.
- Cuidado ao usar .unlink(), pois a remoção é direta.
- Evite caracteres especiais incompatíveis com Windows (: * ?).

------------------------------------------------------------
4. PRÓXIMOS PASSOS
------------------------------------------------------------
Use este conhecimento para criar:
- Organizadores automáticos de downloads.
- Sistemas de backup programados.
- Pipelines de limpeza de logs.

============================================================
Desenvolvido para revisão e prática de automação em Python.
============================================================