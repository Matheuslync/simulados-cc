---
titulo: Heap (heap binário)
grupo: Estrutura de dados
prioridade: alta
ordem: 1
fiap:
  - Fase 6 · Cap 4 — Estruturas avançadas: heaps e tries | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658037
  - Fase 2 · Cap 5 — Busca e ordenação (heap sort) | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604027
links:
  - VisuAlgo — animação de heap binário | https://visualgo.net/en/heap
  - Documentação do heapq (Python) | https://docs.python.org/3/library/heapq.html
---

**O que é:** árvore binária **quase completa** (preenchida nível a nível, da esquerda para a direita) que obedece à **propriedade de heap**:

- **Max-heap:** todo pai ≥ seus filhos → o **maior** elemento fica na raiz.
- **Min-heap:** todo pai ≤ seus filhos → o **menor** fica na raiz. O `heapq` do Python é min-heap.

Não é uma BST: só existe ordem **pai × filho**. Irmãos e subárvores não têm ordem entre si.

**Guardado em vetor** (índice começando em 0):

- filhos de `i` → `2i+1` e `2i+2`
- pai de `i` → `(i-1)//2`

| Operação | Custo |
|---|---|
| Ver o topo (máx/mín) | O(1) |
| Inserir no fim do vetor e subir (**heapify-up**) | O(log n) |
| Remover a raiz: troca com o último e desce (**heapify-down**) | O(log n) |
| Construir heap a partir de um vetor | O(n) |
| Heap sort | O(n log n) em todos os casos, in-place, **não estável** |

**Uso clássico:** fila de prioridade (escalonamento de processos, Dijkstra, eventos por prioridade).

**Heap sort:** 1) transforma o vetor em max-heap; 2) troca a raiz (maior) com o último; 3) reduz o tamanho e aplica heapify-down na raiz; 4) repete.

> **Pegadinhas:** "em um max-heap o menor elemento está em uma folha" → verdade. "O heap está ordenado" → falso. "heapify-down custa O(log n)" → verdade (altura da árvore).
