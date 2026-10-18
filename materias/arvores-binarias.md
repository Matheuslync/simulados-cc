---
titulo: Árvores binárias (BST, AVL, Red-Black)
grupo: Estrutura de dados
prioridade: alta
ordem: 4
fiap:
  - Fase 3 · Cap 4 — Árvores e tabelas hash | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609778
  - Fase 2 · Cap 5 — Busca binária | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604027
links:
  - VisuAlgo — BST e AVL | https://visualgo.net/en/bst
  - Visualização de Red-Black Tree (USFCA) | https://www.cs.usfca.edu/~galles/visualization/RedBlack.html
---

**Vocabulário:** raiz, nó, folha (sem filhos), grau (nº de filhos), profundidade (distância até a raiz), altura (maior caminho até uma folha), subárvore. Árvore não tem ciclos.

**Árvore binária:** cada nó tem no máximo 2 filhos (esquerdo e direito).

**BST (árvore binária de busca):** menores à **esquerda**, maiores à **direita**. A busca "corta pela metade" como a busca binária.

- Inserir 30, 20, 40, 10, 25 → raiz 30; 20 à esquerda; 40 à direita; 10 à esquerda de 20; 25 à direita de 20.
- Percurso **em ordem** (esq, raiz, dir) devolve os valores **ordenados**. Pré-ordem: raiz, esq, dir. Pós-ordem: esq, dir, raiz.
- Inserir em ordem crescente (10, 20, 30, 40, 50) → tudo vai para a direita → vira uma "lista" com altura n → **O(n)**. É o **problema do desbalanceamento**.

**AVL** (Adelson-Velsky e Landis, 1962): fator de balanceamento `BF = altura(esq) − altura(dir)` deve ser **−1, 0 ou 1**. Saiu disso → **rotações** (simples à esquerda/direita, duplas esquerda-direita/direita-esquerda). Balanceamento **rígido** → altura ≈ 1,44 log n → buscas mais rápidas, porém mais rotações.

**Red-Black (rubro-negra):**

- todo nó é vermelho ou preto; a raiz é preta; as folhas NIL são pretas;
- nó vermelho não tem filho vermelho;
- todo caminho até as folhas tem o mesmo número de nós pretos (black-height);
- nó novo entra **vermelho**.

Balanceamento **mais relaxado** (altura ≤ 2 log n) → **menos rotações**, melhor quando há muitas inserções e remoções.

| | BST balanceada / AVL / Red-Black | BST degenerada |
|---|---|---|
| Busca, inserção, remoção | O(log n) | O(n) |

**Busca binária em vetor:** exige o vetor **ordenado**; compara com o elemento do meio e descarta metade a cada passo → O(log n). Com 1.024 elementos, no máximo ~10 comparações.
