📂 Manipulação de Arquivos com Pathlib (versão simplificada)

Este projeto mostra exemplos práticos de como usar o Pathlib no Python para trabalhar com arquivos e pastas.

🧠 O que é o Pathlib?

É uma biblioteca padrão do Python que facilita lidar com caminhos de arquivos de forma mais simples e organizada (orientada a objetos).

✅ Por que usar?
Código mais limpo e fácil de entender
Funciona melhor em diferentes sistemas (Windows, Linux, etc.)
Resolve tarefas comuns como:
organizar arquivos
renomear
buscar
compactar
📚 O que você vai aprender

Cada arquivo (ex01.py até ex11.py) mostra uma ideia prática:

Ex01: conceitos básicos (criar caminhos, verificar arquivos)
Ex02–Ex05: renomear arquivos (simples, com pastas e datas)
Ex06: mudar extensão de arquivos
Ex07: criar vários arquivos
Ex08–Ex09: compactar e extrair ZIP
Ex10: buscar arquivos
Ex11: apagar arquivos automaticamente
⚠️ Cuidados importantes
Verifique se é arquivo antes de mexer (is_file())
Evite sobrescrever sem querer
Tenha cuidado ao deletar (unlink())
Valide arquivos ao extrair ZIP
🚀 Evolução do projeto

Você começa com o básico e avança até tarefas reais, como automação de arquivos.

💡 Próximos passos

Você pode transformar isso em:

ferramenta de linha de comando
organizador automático de arquivos
sistema de backup
📌 Resumo

Aprender pathlib ajuda muito em automação e manipulação de arquivos no Python — é uma ferramenta essencial no dia a dia.
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

