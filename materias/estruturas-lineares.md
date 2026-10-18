---
titulo: "Estruturas lineares: vetor, pilha, fila, lista"
grupo: Estrutura de dados
prioridade: media
ordem: 13
fiap:
  - Fase 2 · Cap 4 — Linguagem C e estruturas lineares | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604026
  - Fase 4 · Cap 2 — Vetores, listas, tuplas e dicionários em Python | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617908
links:
  - VisuAlgo — lista, pilha e fila | https://visualgo.net/en/list
---

- **Vetor (array):** posições contíguas, acesso por índice O(1), tamanho fixo em C.
- **Pilha (stack) — LIFO:** último a entrar, primeiro a sair. `push`/`pop`/`top` em O(1). Trabalha **sempre pelo topo**. Ex.: desfazer (Ctrl+Z), pilha de chamadas de função.
- **Fila (queue) — FIFO:** primeiro a entrar, primeiro a sair. Atende **pela ordem de chegada**. Ex.: fila de impressão, **BFS**.
- **Lista encadeada simples:** cada nó guarda **o valor e um ponteiro para o próximo nó**. Inserir/remover no início O(1); acessar o k-ésimo O(n).

**Busca linear** em vetor desordenado: percorre um a um → O(n), funciona sem ordenação.
