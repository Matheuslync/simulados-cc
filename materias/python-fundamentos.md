---
titulo: "Python: fundamentos e leitura de código"
grupo: Python
prioridade: alta
ordem: 7
fiap:
  - Fase 1 · Cap 4 — Algoritmos, operadores e primeiros programas | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586182
  - Fase 1 · Cap 5 — Estruturas de decisão | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586183
  - Fase 2 · Cap 3 — Estruturas de repetição | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604025
  - Fase 3 · Cap 3 — Subalgoritmos, funções e recursão | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609777
  - Fase 4 · Cap 2 — Listas, tuplas e dicionários | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617908
links:
  - Tutorial oficial de Python (pt-br) | https://docs.python.org/pt-br/3/tutorial/index.html
  - Python Tutor — veja o código executar passo a passo | https://pythontutor.com/visualize.html
---

**Operadores**

- Aritméticos: `+ - *`, `/` (sempre float), `//` (divisão inteira), `%` (resto), `**` (potência). `7//2 = 3`, `7%2 = 1`, `7/2 = 3.5`, `2**3 = 8`.
- Relacionais: `== != > < >= <=` → `bool`.
- Lógicos: `and`, `or`, `not`. Associação: `in`, `not in`. Identidade: `is`, `is not` (mesmo objeto, não só mesmo valor).
- Precedência: `**` → `* / // %` → `+ -` → relacionais → `not` → `and` → `or`. Ex.: `2 + 3 * 2 ** 2 = 14`.

**Tipos:** `int`, `float`, `str`, `bool`. `input()` sempre devolve **str** → converter com `int()` / `float()`. Python tem tipagem dinâmica. Formatação: `"Total {}".format(x)` ou `f"Total {x}"`.

**Decisão:** `if` simples, composto (`else`), encadeado (`elif`). A **indentação** define o bloco.

**Repetição**

- `while cond:` repete enquanto a condição for verdadeira (cuidado com laço infinito).
- `for i in range(ini, fim, passo)` — o `fim` **não entra**: `range(0, 5)` → 0..4; `range(1, 10, 3)` → 1, 4, 7.
- `break` sai do laço; `continue` pula para a próxima volta.

**Subalgoritmos**

- **Procedimento** não retorna valor; **função** retorna (`return`).
- Parâmetro **formal** = o da definição; **real** (argumento) = o da chamada.
- Parâmetro default: `def f(x, y=2)`.
- **Recursão:** a função chama a si mesma e precisa de **condição de parada**.
- Importar: `import modulo`, `from modulo import f`, `from modulo import *`.

**Coleções**

| | Sintaxe | Mutável? | Observação |
|---|---|---|---|
| list | `[1, 2]` | sim | `append`, `insert`, `pop`, `extend`, `count` |
| tuple | `(1, 2)` | **não** | indexação funciona: `(10,20,30)[2]` → 30 |
| dict | `{"k": 1}` | sim | `d.get("x", 0)` evita erro |
| set | `{1, 2}` | sim | sem repetição |

Índices começam em 0; `l[-1]` é o último; a fatia `l[1:3]` pega os índices 1 e 2.

**Atenção:** `b = a` não copia a lista — os dois nomes apontam para o mesmo objeto.

**Python × C:** Python é interpretado e de tipagem dinâmica; C é compilado, tipagem estática, usa `;` e chaves e precisa de `main()`.
