🧠 O que é o Pathlib?

pathlib é uma biblioteca padrão do Python que permite manipular caminhos de arquivos de forma mais moderna e organizada.

Ele substitui o os.path e torna o código:

Mais fácil de ler
Mais seguro
Compatível com diferentes sistemas
🚀 Por que usar?

Manipular arquivos é comum em projetos, como:

Organizar pastas
Processar dados
Gerenciar arquivos
Compactar e extrair arquivos
Limpar arquivos desnecessários

O pathlib facilita tudo isso com uma sintaxe simples.

📚 Exemplos do projeto

Cada arquivo (ex01.py até ex11.py) mostra um conceito:

Ex01: conceitos básicos (Path, exists, propriedades)
Ex02: renomear arquivos
Ex03–04: renomeação baseada em pastas
Ex05: adicionar data no nome
Ex06: trocar extensão
Ex07: criar arquivos em lote
Ex08: compactar arquivos (ZIP)
Ex09: extrair ZIP
Ex10: buscar arquivos
Ex11: apagar arquivos
⚠️ Boas práticas
Verifique se é arquivo (is_file())
Evite sobrescrever sem necessidade
Cuidado ao apagar arquivos (unlink())
Valide arquivos ao extrair ZIP
Evite caracteres inválidos
📈 Evolução do aprendizado

O projeto segue esta ordem:

Conceitos básicos
Navegação em pastas
Manipulação de nomes
Automação
Casos reais (ZIP, busca, limpeza)
# Manipulação de Arquivos com Pathlib (Python)

Exemplos práticos usando `pathlib` para trabalhar com arquivos e diretórios no Python — do básico ao uso real.

---

## O que é Pathlib?

Biblioteca padrão do Python para manipulação de caminhos de forma **simples, legível e orientada a objetos**.
Substitui o `os.path` com uma API mais moderna.

---

## Para que serve?

* Organizar arquivos e pastas
* Automatizar tarefas
* Processar dados
* Compactar e extrair arquivos
* Limpar diretórios

---

## Exemplos

Cada arquivo (`ex01.py` até `ex11.py`) mostra um caso prático:

* **Ex01** — Conceitos básicos (`Path`, `exists`, propriedades)
* **Ex02–Ex05** — Renomeação de arquivos (simples, com contexto e data)
* **Ex06** — Alteração de extensão
* **Ex07** — Criação de arquivos em lote
* **Ex08–Ex09** — Compactação e extração (ZIP)
* **Ex10** — Busca de arquivos
* **Ex11** — Limpeza de arquivos

---

## Boas práticas

* Verifique com `is_file()` antes de agir
* Evite sobrescrever arquivos
* Cuidado com `unlink()` (remove arquivos)
* Valide arquivos ao extrair ZIP

---

## Progressão

1. Fundamentos
2. Navegação
3. Manipulação
4. Automação
5. Casos reais

---

## Ideias para evoluir

* CLI (linha de comando)
* Organizador de arquivos
* Sistema de backup
* Pipeline de dados

---

## Conclusão

`pathlib` é essencial para automação e manipulação de arquivos em Python.
Veja os exemplos para aprender na prática.

