# 🎓 Cadastro de Alunos

Coleção de sistemas de terminal em Python para cadastrar, listar, alterar e excluir alunos, com notas e situação (aprovado, recuperação ou reprovado). Cada arquivo é uma versão do mesmo tema, com estilos de código e critérios de avaliação diferentes.

---

## 🧭 Versões do projeto

| Arquivo | Versão | Armazenamento | Situação calculada |
|---|---|---|---|
| `cadastro_aluno.py` | Lista em memória com relatório final | Não grava em arquivo | ≥ 7 aprovado · 5 a 6,9 recuperação · < 5 reprovado |
| `cadastroCOR_dupla.py` | CRUD colorido, feito em dupla | `dados_alunos.txt` | ≥ 6 aprovado · < 6 reprovado |
| `cadastroCOR_comentado.py` | CRUD colorido, versão comentada do Exercício 28 | `alunos.txt` (formato de tabela) | ≥ 6 aprovado · < 6 reprovado |
| `projetoex28.py` | Rascunho do cadastro de produtos (classe `Produto`) | Não grava em arquivo | — |

> A versão comentada (`cadastroCOR_comentado.py`) é a mais completa do conjunto e a recomendada para uso.

---

## 🧰 Requisitos

- Python 3.8 ou superior
- [colorama](https://pypi.org/project/colorama/), exigido pelas versões coloridas e pelo rascunho de produtos:

```bash
pip install colorama
```

`cadastro_aluno.py` não usa nenhuma biblioteca externa.

---

## 🚀 Como executar

Dentro da pasta do projeto, escolha a versão e rode:

```bash
python cadastroCOR_comentado.py
```

Use os números do menu para navegar. A opção `0` encerra o programa.

---

## ✨ Funcionalidades

### `cadastro_aluno.py`

- Cadastra alunos em sequência, perguntando após cada um se deseja adicionar outro.
- Ao final, mostra um relatório com:
  - lista de alunos, com idade, nota e situação;
  - média da sala;
  - quantidade de aprovados, em recuperação e reprovados;
  - aluno com a maior e a menor nota.

### `cadastroCOR_dupla.py`

Menu com as opções:

1. Cadastrar aluno (nome, idade e nota)
2. Listar alunos
3. Alterar aluno (o novo nome é opcional, basta apertar ENTER para manter)
4. Excluir aluno (pede confirmação com `S` ou `N`)

### `cadastroCOR_comentado.py`

Menu com as opções:

1. Cadastrar aluno (nome e nota)
2. Listar alunos em tabela, com resumo da turma
3. Alterar aluno (nome e nota)
4. Excluir aluno

A listagem mostra:
- total de alunos;
- quantidade de aprovados e reprovados;
- aluno com a maior nota;
- aluno com a menor nota.

### `projetoex28.py`

Trecho inicial do cadastro de produtos. Contém a classe `Produto`, com nome e preço, e a função `cadastrarprod()`, que valida os dados digitados. Ainda não possui menu nem gravação em arquivo.

---

## 📁 Estrutura

```
cadastro_aluno-main/
├── cadastro_aluno.py          # versão em memória com relatório
├── cadastroCOR_dupla.py       # CRUD colorido (dados_alunos.txt)
├── cadastroCOR_comentado.py   # CRUD colorido comentado (alunos.txt)
└── projetoex28.py             # rascunho de cadastro de produtos
```

Os arquivos de dados são criados automaticamente na pasta de execução, na primeira vez em que o programa roda.

---

## 🗃️ Formato dos dados

**`dados_alunos.txt`** (`cadastroCOR_dupla.py`), uma linha por aluno:

```
Maria Silva;8.50
```

**`alunos.txt`** (`cadastroCOR_comentado.py`), em formato de tabela, com cabeçalho de comentários:

```
NOME                                | NOTA     | SITUACAO   
------------------------------------+----------+-----------
Maria Silva                         |  8.50    | APROVADO   
```

A situação é sempre recalculada a partir da nota. Por isso, não é necessário alterá-la manualmente no arquivo.

---

## ✅ Regras de preenchimento

- **Nome:** obrigatório, somente letras e espaços. É formatado com inicial maiúscula em cada palavra.
- **Idade** (`cadastro_aluno.py`): número inteiro maior que zero.
- **Nota:** número de 0 a 10. Aceita vírgula ou ponto como separador decimal (ex.: `8,5` ou `8.5`).
- **Busca para alterar e excluir:** feita pelo nome, sem diferenciar maiúsculas de minúsculas.

---

## 🎨 Visual

As versões coloridas usam [colorama](https://pypi.org/project/colorama/) para:
- menus e tabelas com bordas Unicode;
- situação em verde (aprovado) e vermelho (reprovado);
- mensagens de sucesso, aviso e erro com cores próprias.
