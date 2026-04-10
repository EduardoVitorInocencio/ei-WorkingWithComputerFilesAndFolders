# 📁 Pathlib na prática

## Sobre o projeto
Este repositório contém exemplos práticos de uso do **pathlib** em Python para trabalhar com **arquivos e diretórios**.  
Os exemplos vão do básico até situações comuns do dia a dia.

## O que é o pathlib
- Biblioteca padrão do Python
- Trabalha com caminhos usando objetos
- Substitui o uso de `os.path`

### Vantagens
- Código mais legível
- Mais seguro
- Funciona bem em diferentes sistemas operacionais

## Por que usar pathlib
Muito usado em projetos reais, como:
- Organização de pastas
- Processamento de dados
- Gerenciamento de arquivos e mídia
- Compactação e extração de arquivos
- Limpeza de diretórios

A API é simples e poderosa.

## Estrutura do repositório
- Os exemplos seguem o padrão `exXX.py`
- Cada arquivo cobre um conceito específico

## Exemplos disponíveis
- **Ex01** – Introdução e navegação com `Path`
- **Ex02** – Renomear arquivos
- **Ex03** – Renomear usando a pasta pai
- **Ex04** – Nome baseado na hierarquia de pastas
- **Ex05** – Renomear com timestamp
- **Ex06** – Alterar extensão de arquivos
- **Ex07** – Criar vários arquivos
- **Ex08** – Compactar arquivos (ZIP)
- **Ex09** – Extrair arquivos ZIP
- **Ex10** – Buscar arquivos com `rglob()`
- **Ex11** – Deletar arquivos com `unlink()`

## Boas práticas
- Sempre verificar se é arquivo (`is_file()`)
- Evitar sobrescrever arquivos sem necessidade
- Ter cuidado com operações destrutivas
- Validar caminhos ao extrair ZIP
- Usar nomes de arquivos válidos

## Caminho de aprendizado
1. Conceitos básicos
2. Navegação em diretórios
3. Manipulação de nomes
4. Automação
5. Casos reais (ZIP, busca, limpeza)

## Próximos passos
- Criar uma CLI (linha de comando)
- Organizador de downloads
- Sistema de backup
- Pipeline de processamento de arquivos

## Conclusão
O **pathlib** é essencial para trabalhar com:
- Automação
- Dados
- Sistema de arquivos

Explore os exemplos para fixar o aprendizado.

## Autor
Projeto criado para revisar e praticar manipulação de arquivos em Python.