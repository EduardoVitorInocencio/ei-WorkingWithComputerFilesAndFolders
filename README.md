## Visão geral
- Repositório com exemplos práticos usando `pathlib` no Python  
- Foco em manipulação de arquivos e diretórios  
- Abordagem progressiva: do básico a cenários reais  

## O que é o Pathlib
- Biblioteca padrão do Python  
- Trabalha com caminhos de forma orientada a objetos  
- Substitui `os.path`  
- Benefícios:
  - Código mais legível  
  - Mais seguro  
  - Mais portátil  

## Por que usar
- Essencial em projetos reais para:
  - Organização de diretórios  
  - Processamento de dados (ETL)  
  - Gerenciamento de mídia  
  - Compactação e extração  
  - Limpeza de arquivos  
- API simples e poderosa  

## Estrutura dos exemplos
- Arquivos `exXX.py`, cada um com um conceito específico  

### Conteúdo dos exemplos
- Ex01: Introdução ao `Path`, propriedades e navegação  
- Ex02: Renomeação de arquivos  
- Ex03: Renomeação baseada na pasta pai  
- Ex04: Nome baseado na hierarquia de pastas  
- Ex05: Renomeação com timestamp  
- Ex06: Alteração de extensão de arquivos  
- Ex07: Criação de múltiplos arquivos  
- Ex08: Compactação com `zipfile`  
- Ex09: Extração de arquivos ZIP  
- Ex10: Busca de arquivos com `rglob()`  
- Ex11: Limpeza de arquivos com `unlink()`  

## Boas práticas
- Verificar se é arquivo (`is_file()`)  
- Evitar sobrescrever arquivos desnecessariamente  
- Cuidado com operações destrutivas  
- Validar caminhos ao extrair ZIP  
- Evitar caracteres inválidos em nomes  

## Evolução do aprendizado
1. Fundamentos  
2. Navegação em diretórios  
3. Manipulação de nomes  
4. Automação  
5. Operações reais (ZIP, busca, limpeza)  

## Próximos passos
- Criar CLI (linha de comando)  
- Organizador de downloads  
- Sistema de backup  
- Pipeline de processamento de arquivos  

## Conclusão
- `pathlib` é essencial para trabalhar com:
  - Automação  
  - Dados  
  - Sistema de arquivos  
- Recomenda-se explorar os exemplos práticos  

## Autor
- Projeto focado em revisão de manipulação de arquivos com Python