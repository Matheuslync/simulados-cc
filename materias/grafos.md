---
titulo: "Grafos: BFS, DFS e Dijkstra"
grupo: Estrutura de dados
prioridade: media
ordem: 15
fiap:
  - Fase 4 · Cap 3 — Grafos e rotas de distribuição | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617909
links:
  - VisuAlgo — BFS e DFS | https://visualgo.net/en/dfsbfs
  - VisuAlgo — caminho mínimo (Dijkstra) | https://visualgo.net/en/sssp
---

G = (V, E): vértices + arestas. Pode ser direcionado ou não, ponderado ou não.

- **Matriz de adjacência:** V×V; testa se existe aresta em O(1); memória O(V²) — boa para grafos densos.
- **Lista de adjacência:** memória O(V + E) — boa para grafos esparsos.

**Percursos**

- **BFS (busca em largura):** usa **fila**, visita por níveis, acha o **menor caminho em número de arestas** (grafo não ponderado). O(V + E).
- **DFS (busca em profundidade):** usa **pilha** ou recursão; vai fundo antes de voltar. Útil para componentes conexas e ciclos.

**Dijkstra:** menor caminho a partir de uma origem com pesos **não negativos**. Com peso negativo não funciona (use Bellman-Ford). Com fila de prioridade (heap): O((V + E) log V).
