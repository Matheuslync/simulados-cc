---
titulo: Complexidade, busca e ordenação
grupo: Estrutura de dados
prioridade: media
ordem: 14
fiap:
  - Fase 2 · Cap 5 — Complexidade, busca e ordenação | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604027
  - Fase 6 · Cap 3 — Complexidade: O, Ω, Θ, recorrências e teorema mestre | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658036
links:
  - VisuAlgo — algoritmos de ordenação animados | https://visualgo.net/en/sorting
  - Big-O Cheat Sheet | https://www.bigocheatsheet.com/
---

**Big-O** descreve como o custo cresce com o tamanho da entrada n (normalmente o pior caso, sem constantes):

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)

- **Busca linear:** O(n), não precisa estar ordenado.
- **Busca binária:** O(log n), **exige vetor ordenado**.

| Algoritmo | Melhor | Médio | Pior | Observação |
|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | troca vizinhos; simples, lento |
| Selection | O(n²) | O(n²) | O(n²) | escolhe o menor e põe na frente |
| Insertion | O(n) | O(n²) | O(n²) | ótimo para quase ordenado |
| Merge | O(n log n) | O(n log n) | O(n log n) | divide e conquista, estável, memória extra |
| Quick | O(n log n) | O(n log n) | **O(n²)** | pivô ruim degrada |
| Heap | O(n log n) | O(n log n) | O(n log n) | usa heap, in-place |

Desvantagem típica dos algoritmos simples (bubble, selection, insertion): **O(n²)**, ficam lentos com muitos dados.

**Notação assintótica (Fase 6)**

| Notação | Significa | Analogia |
|---|---|---|
| **O(g)** | limite **superior** — cresce no máximo como g | ≤ |
| **Ω(g)** | limite **inferior** — cresce no mínimo como g | ≥ |
| **Θ(g)** | limite **justo** — O e Ω ao mesmo tempo | = |

Constantes e termos menores são ignorados: `3n² + 5n + 2` é Θ(n²). Analisa-se **tempo** e também **espaço** (memória extra).

**Recorrências** descrevem algoritmos recursivos: busca binária `T(n) = T(n/2) + O(1)` → **Θ(log n)**; merge sort `T(n) = 2T(n/2) + n` → **Θ(n log n)**.

**Teorema mestre** para `T(n) = a·T(n/b) + f(n)` (a ≥ 1, b > 1): compare f(n) com **n^(log_b a)**.

1. f(n) cresce **mais devagar** → `T(n) = Θ(n^(log_b a))` (dominam as folhas).
2. f(n) cresce **igual** → `T(n) = Θ(n^(log_b a) · log n)`.
3. f(n) cresce **mais rápido** (com condição de regularidade) → `T(n) = Θ(f(n))` (domina a raiz).

Exemplos: `4T(n/2) + n` → n^(log₂4) = n² > n → Θ(n²) · `2T(n/2) + n` → caso 2 → Θ(n log n) · `2T(n/2) + n²` → caso 3 → Θ(n²).

**Análise amortizada:** custo médio por operação em uma **sequência** de operações. Ex.: `append` em vetor dinâmico às vezes precisa realocar (caro), mas em média é **O(1) amortizado**.

**Na prática:** medir tempo com `clock()` em C e comparar o crescimento (ex.: um O(n²) fica ~4× mais lento ao dobrar n).

