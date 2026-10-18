---
titulo: Linguagem C
grupo: Programação
prioridade: media
ordem: 24
fiap:
  - Fase 2 · Cap 4 — Linguagem C: tipos, laços, condicionais e funções | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604026
  - Fase 6 · Cap 3 — Medição de desempenho em C com clock() | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658036
links:
  - Referência da linguagem C (cppreference) | https://en.cppreference.com/w/c
---

C é **compilada** (ex.: `gcc programa.c -o programa`), de **tipagem estática** e **estruturada**: sequência, seleção (`if/else`, `switch`) e repetição (`for`, `while`, `do…while`). Toda instrução termina com `;` e os blocos ficam entre `{ }`. O programa começa em `int main()`, que normalmente retorna 0.

**Tipos fundamentais:** `char` (1 byte), `int` (geralmente 4 bytes), `float`, `double` (mais precisão). Modificadores: `short`, `long`, `unsigned`. Booleano: `#include <stdbool.h>` ou 0 = falso, qualquer outro valor = verdadeiro.

**Entrada e saída:** `printf("%d", x)` e `scanf("%d", &x)` — o `&` passa o endereço da variável. Formatos: `%d` int · `%f` float · `%lf` double (no scanf) · `%c` char · `%s` string.

**Laços**

| Laço | Executa | Uso típico |
|---|---|---|
| `while (cond)` | **0 ou mais** vezes | não se sabe quantas vezes |
| `do { } while (cond);` | **1 ou mais** vezes (testa no fim) | validar entrada |
| `for (init; cond; atualização)` | contado | percorrer vetor |

`break` sai do laço; `continue` vai para a próxima volta.

**switch:** compara um valor inteiro/char com `case`s. **Sem `break`, a execução "cai" no próximo case.** `default` trata os demais.

**Funções:** o **protótipo** (`int soma(int a, int b);`) declara antes do `main`; a definição pode vir depois. `void` = sem retorno ou sem parâmetros.

**Vetores e strings:** índice começa em 0; acessar fora do tamanho é erro (comum com `<=` no `for`). String é vetor de `char` terminado em `'\0'`.

**Medir tempo:** `clock()` de `<time.h>`; tempo em segundos = `(fim − inicio) / CLOCKS_PER_SEC`.
