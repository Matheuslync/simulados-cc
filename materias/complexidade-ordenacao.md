---
titulo: Complexidade, busca e ordenação
grupo: Estrutura de dados
prioridade: media
ordem: 14
fiap:
  - Fase 2 · Cap 5 — Complexidade, busca e ordenação | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604027
  - Fase 6 · Cap 3 — Complexidade computacional | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658036
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
