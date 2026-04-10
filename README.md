📂 Automação e Manipulação de Arquivos com Pathlib
Este repositório é um guia prático e progressivo sobre a biblioteca pathlib. O objetivo é demonstrar como substituir métodos arcaicos (como os.path) por uma abordagem orientada a objetos, tornando a automação de sistemas de arquivos mais elegante e robusta.

🧠 Por que abandonar o os.path?
O pathlib trata caminhos não apenas como strings, mas como objetos. Isso traz vantagens imediatas:

Legibilidade: Código que parece uma frase, não uma concatenação complexa.

Portabilidade: O mesmo código funciona perfeitamente em Windows, Linux e macOS.

Segurança: Métodos integrados para evitar erros comuns de permissão e existência.

🛠️ O que você vai encontrar aqui?
O aprendizado é dividido em 11 módulos práticos. Cada script exXX.py resolve um problema real:

🔰 Nível 1: Fundamentos
Ex01 — Introdução: Atributos básicos (stem, suffix, name) e verificação de existência.

Ex07 — Criação em lote: Como utilizar o touch() para gerar arquivos rapidamente.

Ex10 — Busca Avançada: Diferença entre glob e rglob para varreduras recursivas.

🔄 Nível 2: Transformação
Ex02 a 04 — Renomeação Inteligente: Desde trocas simples até nomes baseados na hierarquia de pastas.

Ex05 — Timestamps: Integração com stat() para nomear arquivos com base na data de criação.

Ex06 — Conversão de Extensões: O poder do with_suffix() para migrar formatos (ex: .txt → .csv).

📦 Nível 3: Operações de Sistema
Ex08 & 09 — Gestão de Pacotes: Compactação e extração de arquivos .zip de forma automatizada.

Ex11 — Sanitização: Limpeza segura de diretórios e remoção de resíduos com unlink().

🚀 Como utilizar este repositório
Clone o projeto:

Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
Explore a evolução:
Recomendamos abrir os arquivos na ordem numérica, pois os conceitos de um script são frequentemente reutilizados no próximo.

Execute um exemplo:

Bash
python ex01.py
⚠️ Checklist de Boas Práticas
Ao automatizar arquivos, sempre lembre-se:

[x] Validar tipos: Use is_file() ou is_dir() antes de operar.

[x] Tratar exceções: Arquivos podem estar abertos ou protegidos pelo sistema.

[x] Cuidado Destrutivo: Antes de um unlink(), faça um print do que será apagado para conferir.

[x] Encoding: Ao ler arquivos, prefira sempre encoding='utf-8'.

🎯 Próximos Desafios
Quer levar esse conhecimento além? Tente implementar:

Organizador de Downloads: Um script que move arquivos para pastas "Imagens", "Documentos" e "PDFs" automaticamente.

Backup Incremental: Copiar apenas arquivos alterados nas últimas 24 horas.

CLI Tool: Transformar esses exemplos em uma ferramenta de linha de comando usando argparse ou click.

🧑‍💻 Autor
Desenvolvido para fins de estudo e revisão das melhores práticas em Python. Sinta-se à vontade para contribuir com novos exemplos!