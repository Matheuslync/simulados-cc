---
titulo: Portas lógicas e bases numéricas
grupo: Lógica digital
prioridade: media
ordem: 16
fiap:
  - Fase 1 · Cap 3 — Sistemas numéricos e bases | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586181
  - Fase 2 · Cap 2 — Lógica booleana e portas lógicas | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604024
  - Fase 6 · Cap 10 — Conversões numéricas | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658043
links:
  - Simulador de circuitos lógicos (Logic.ly) | https://logic.ly/demo/
---

| Porta | Saída 1 quando… |
|---|---|
| AND | todas as entradas = 1 |
| OR | pelo menos uma = 1 |
| NOT | a entrada = 0 |
| NAND / NOR | negação do AND / OR (portas universais). NOR = NOT(A OR B) |
| XOR | entradas diferentes |
| XNOR | entradas iguais |

n entradas → **2ⁿ linhas** na tabela-verdade (3 entradas → 8). `X = A · B` é uma operação **AND**.

**Bases numéricas:** sistema posicional — cada posição vale uma potência da base. O subscrito indica a base (`1011₂` = binário).

- 1011₂ = 8 + 0 + 2 + 1 = **11**
- 122₈ = 1·64 + 2·8 + 2 = **82**
- Hexa usa A–F (A = 10 … F = 15). 1 dígito hexa = 4 bits; 1 dígito octal = 3 bits.
- Decimal → binário: divisões sucessivas por 2, lendo os restos de baixo para cima.
- No decimal, o algarismo mais à direita está na ordem das **unidades** (10⁰).
