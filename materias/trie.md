---
titulo: Trie (árvore de prefixos)
grupo: Estrutura de dados
prioridade: alta
ordem: 2
fiap:
  - Fase 6 · Cap 4 — Estruturas avançadas: heaps e tries | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658037
links:
  - Trie na Wikipédia | https://pt.wikipedia.org/wiki/Trie
  - Visualização interativa de trie (USFCA) | https://www.cs.usfca.edu/~galles/visualization/Trie.html
---

**O que é:** árvore em que cada nível representa **um caractere**. O caminho da raiz até um nó forma um **prefixo**. Um marcador `fim` indica que ali termina uma palavra completa.

Exemplo: inserir *casa* e *casaco*. As duas compartilham o caminho `c → a → s → a` (o nó do segundo "a" tem `fim = 1`) e depois *casaco* continua com `c → o`.

| Operação | Custo |
|---|---|
| Inserir / buscar palavra de tamanho m | **O(m)**, não depende de quantas palavras há |
| Listar todas as palavras com um prefixo | O(m + resultados) |

**Como o material implementa (C):**

- cada nó tem um vetor `filhos[26]`; o índice da letra é `c - 'a'`;
- **inserir:** percorre a palavra; se o filho é `NULL`, cria o nó; no final marca `fim = 1`;
- **buscar:** percorre sem criar nada; se achar `NULL` a palavra não existe; no final só é palavra se `fim == 1` (senão é apenas prefixo).

**Aplicações:** autocompletar, corretor ortográfico, dicionários, **roteamento (longest prefix match)**.

**Trie × hash:** a trie permite busca por prefixo e ordem alfabética; a hash não. Em compensação a trie **gasta mais memória** (muitos ponteiros por nó).

> **Na prova:** "estrutura ideal para autocompletar / busca por prefixo" → **Trie**. "Fila de prioridade / pegar o maior rápido" → **Heap**.
