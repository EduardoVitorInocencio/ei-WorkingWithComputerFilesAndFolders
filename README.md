# 📂 Manipulação de Arquivos com Pathlib (Python)

Este repositório contém uma coleção de exemplos práticos utilizando a biblioteca `pathlib` do Python para manipulação de arquivos e diretórios.

O objetivo é demonstrar, de forma progressiva, como automatizar tarefas comuns do dia a dia, evoluindo de operações simples até cenários mais próximos do mundo real.

---

## 🧠 O que é o Pathlib?

O `pathlib` é uma biblioteca padrão do Python que fornece uma forma **orientada a objetos** para lidar com caminhos de arquivos e diretórios.

Ele substitui abordagens mais antigas como `os.path`, tornando o código:

- Mais legível
- Mais seguro
- Mais portátil

---

## Por que usar Pathlib?

Em projetos reais, manipulação de arquivos é essencial:

- Organização de diretórios
- Processamento de dados (ETL)
- Gerenciamento de mídia
- Compactação e extração de arquivos
- Limpeza de arquivos temporários

O `pathlib` facilita todas essas tarefas com uma API simples e poderosa.

---

## 📚 Estrutura dos Exemplos

Cada arquivo `exXX.py` aborda um conceito específico.  
Se quiser se aprofundar, abra o arquivo correspondente.

---

### 🔹 Ex01 — Introdução ao Pathlib

- Criação de caminhos com `Path`
- Verificação de existência (`exists`)
- Leitura de propriedades:
  - `name`
  - `stem`
  - `suffix`
- Navegação com `iterdir()`

📌 Veja: `ex01.py`

---

### 🔹 Ex02 — Renomeação de arquivos

- Iteração em diretórios
- Criação de novos nomes
- Uso de `rename()`

📌 Veja: `ex02.py`

---

### 🔹 Ex03 — Renomeação com base na pasta pai

- Uso de `glob('**/*.txt')`
- Estrutura de caminhos (`parts`)
- Automação baseada em contexto

📌 Veja: `ex03.py`

---

### 🔹 Ex04 — Nome baseado na hierarquia

- Extração de subpastas
- Construção dinâmica de nomes
- Transformação da estrutura em nome

📌 Veja: `ex04.py`

---

### 🔹 Ex05 — Renomeação com timestamp

- Uso de `stat()`
- Manipulação de datas com `datetime`
- Padronização de nomes com data

📌 Veja: `ex05.py`

---

### 🔹 Ex06 — Alteração de extensão

- Uso de `with_suffix()`
- Conversão de arquivos (.txt → .csv)

📌 Veja: `ex06.py`

---

### 🔹 Ex07 — Criação de múltiplos arquivos

- Uso de `touch()`
- Geração de arquivos em lote

📌 Veja: `ex07.py`

---

### 🔹 Ex08 — Compactação de arquivos

- Uso de `zipfile`
- Criação de arquivos `.zip`
- Remoção de arquivos após compactação

📌 Veja: `ex08.py`

---

### 🔹 Ex09 — Extração de arquivos ZIP

- Leitura de arquivos compactados
- Extração com `extractall()`
- Organização por diretórios

📌 Veja: `ex09.py`

---

### 🔹 Ex10 — Busca de arquivos

- Busca recursiva com `rglob()`
- Filtro por nome (`stem`)
- Uso de caminhos absolutos

📌 Veja: `ex10.py`

---

### 🔹 Ex11 — Limpeza de arquivos

- Remoção de arquivos com `unlink()`
- Automação de limpeza em diretórios

📌 Veja: `ex11.py`

---

## ⚠️ Boas práticas importantes

- Sempre verificar se é arquivo (`is_file()`)
- Evitar sobrescrever arquivos sem necessidade
- Cuidado com operações destrutivas (`unlink()`)
- Validar caminhos ao extrair arquivos ZIP
- Evitar caracteres inválidos (ex: `:` no Windows)

---

## 🧠 Evolução prática

Este repositório segue uma progressão:

1. Fundamentos (`Path`)
2. Navegação em diretórios
3. Manipulação de nomes
4. Automação de arquivos
5. Operações reais (ZIP, busca, limpeza)

---

## 💡 Próximos passos

Você pode evoluir este projeto para:

- CLI (linha de comando)
- Organizador automático de downloads
- Sistema de backup
- Pipeline de processamento de arquivos

---

## 📌 Conclusão

O domínio de `pathlib` é essencial para qualquer desenvolvedor Python que deseja trabalhar com:

- automação
- dados
- sistemas de arquivos

Explore cada arquivo `.py` para entender a implementação prática.

---

## 🧑‍💻 Autor

Projeto desenvolvido com foco em revisar sobre manipulação de arquivos com Python.