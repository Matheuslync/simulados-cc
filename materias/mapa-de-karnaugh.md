---
titulo: Mapa de Karnaugh
grupo: Lógica digital
prioridade: alta
ordem: 5
fiap:
  - Fase 6 · Cap 2 — Mapa de Karnaugh (principal) | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658035
  - Fase 3 · Cap 2 — Álgebra de Boole, mintermos e maxtermos | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609776
  - Fase 5 · Cap 2 — Teoremas booleanos | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629591
links:
  - Mapa de Karnaugh na Wikipédia | https://pt.wikipedia.org/wiki/Mapa_de_Karnaugh
---

Método **gráfico** para simplificar expressões booleanas a partir da tabela-verdade (alternativa à simplificação algébrica).

**Montagem**

- 2 variáveis → 2×2 (4 células); 3 variáveis → 2×4 (8); 4 variáveis → 4×4 (16).
- Linhas e colunas na ordem do **código Gray: 00, 01, 11, 10** — células vizinhas mudam só 1 bit.
- Coloque **1** nas células dos mintermos (linhas da tabela-verdade com saída 1).

**Regras dos grupos**

- Grupos de **1, 2, 4, 8…** células (potências de 2), em retângulo. Nada de diagonal nem grupo de 3 ou 6.
- Grupos **os maiores possíveis** e o **menor número** de grupos; podem se sobrepor.
- As bordas "dão a volta" (esquerda ↔ direita, cima ↔ baixo). Os **4 cantos** são vizinhos.
- Don't care (X) pode entrar no grupo se ajudar.
- Agrupar **1s** → Soma de Produtos (SOP). Agrupar **0s** → Produto de Somas (POS).

**Leitura:** em cada grupo, fica só a variável que **não muda** (valor 1 → `A`, valor 0 → `A'`). Grupo de 2ᵏ células elimina k variáveis.

```
F(A,B,C) = Σm(0,2,4,6)
       BC: 00  01  11  10
  A=0:     1   0   0   1
  A=1:     1   0   0   1     → grupo de 4 pelas bordas → F = C'
```

Mais exemplos:

| Função | Resultado |
|---|---|
| F(A,B) = Σm(1,2,3) | A + B |
| F(A,B,C) = Σm(3,7) | BC |
| F(A,B,C,D) = Σm(5,7,13,15) | BD |
| F(A,B,C,D) = Σm(0,2,8,10) (os 4 cantos) | B'D' |

**Base algébrica**

- **Mintermo:** produto (AND) de uma linha com saída 1; variável com valor 0 entra **negada**. Soma dos mintermos = soma de produtos.
- **Maxtermo:** soma (OR) de uma linha com saída 0; variável com valor 1 entra negada. Produto dos maxtermos = produto de somas.

**Identidades que caem:** `A + 1 = 1` · `A·0 = 0` · `A + A' = 1` · `A·A' = 0` · `A + AB = A` e `A(A+B) = A` (absorção) · `A + A'B = A + B` · `AB + AB' = A` · `A(B+C) = AB + AC` · De Morgan: `(AB)' = A' + B'` e `(A+B)' = A'B'`.
