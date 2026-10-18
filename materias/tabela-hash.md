---
titulo: Tabela hash
grupo: Estrutura de dados
prioridade: alta
ordem: 3
fiap:
  - Fase 3 · Cap 4 — Árvores e tabelas hash | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609778
links:
  - VisuAlgo — tabela hash (sondagem linear, quadrática, encadeamento) | https://visualgo.net/en/hashtable
  - Tabela de dispersão na Wikipédia | https://pt.wikipedia.org/wiki/Tabela_de_dispers%C3%A3o
---

Guarda pares **chave → valor**. Uma **função hash** `h(k)` transforma a chave em um índice de `0` a `m−1`. Exemplo clássico: `h(k) = k mod m`.

Três peças: **função hash**, **vetor de armazenamento** (buckets) e **tratamento de colisões**.

**Colisão:** duas chaves diferentes caem no mesmo índice. É inevitável; o que importa é como tratar.

- **Encadeamento separado (chaining):** cada posição guarda uma lista com todos os elementos daquele índice.
- **Endereçamento aberto:** procura outra posição livre — sondagem **linear** (+1, +2…), **quadrática** (+1², +2²…) ou **hash duplo**.

**Fator de carga** α = n / m. Quando α cresce, aumentam as colisões → faz-se **rehash** para uma tabela maior.

| | Médio | Pior caso |
|---|---|---|
| Busca / inserção / remoção | **O(1)** | O(n) (tudo colide) |

Boa função hash: determinística, rápida e que **espalha uniformemente** as chaves.

**Hash × árvore balanceada:** hash é mais rápida em média (O(1) contra O(log n)), mas **não mantém ordem**. Para percorrer em ordem ou buscar por intervalo, use árvore.

**Exemplo:** m = 7, inserir 15, 22, 8 com sondagem linear:

```
15 mod 7 = 1 → posição 1
22 mod 7 = 1 (ocupada) → posição 2
 8 mod 7 = 1 (ocupada, ocupada) → posição 3
```

> Em Python, `dict` e `set` são tabelas hash.
