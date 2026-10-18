---
titulo: Derivada e gradiente descendente
grupo: Matemática e IA
prioridade: alta
ordem: 8
fiap:
  - Fase 4 · Cap 4 — Cálculo diferencial e gradiente descendente | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617910
  - Fase 4 · Cap 6 — Regressão logística (otimização via gradiente) | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617912
  - Fase 2 · Cap 6 — Funções e modelos matemáticos | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604028
links:
  - Gradient descent na Wikipédia (inglês) | https://en.wikipedia.org/wiki/Gradient_descent
  - Khan Academy — derivadas | https://pt.khanacademy.org/math/calculus-1
---

**Derivada** `f'(x)` = taxa de variação instantânea = **inclinação da reta tangente** no ponto.

- `f' > 0` → função crescendo; `f' < 0` → decrescendo; `f' = 0` → **ponto crítico**.
- No ponto crítico: `f'' > 0` → **mínimo**; `f'' < 0` → máximo.
- Regras: `(xⁿ)' = n·xⁿ⁻¹` · `(constante)' = 0` · `(eˣ)' = eˣ` · `(ln x)' = 1/x` · `(sen x)' = cos x`.

**Gradiente descendente** (minimizar custo/erro): dar passos na direção **contrária** à derivada, porque a derivada aponta para onde a função cresce.

```
x(k+1) = x(k) − α · f'(x(k))        (várias variáveis: ∇f no lugar de f')
```

- **α (ou η) = taxa de aprendizado:** pequena → converge devagar (muitas iterações); grande → pode **oscilar ou divergir**.
- Usa só informação **local** → pode parar em um **mínimo local**, dependendo do **ponto inicial**.
- **Gradiente** = vetor das derivadas parciais; aponta para o **maior crescimento**; é perpendicular às curvas de nível.

**Exemplo:** `f(x) = x²`, `x₀ = 3`, `α = 0,1`:

| k | x | f'(x) = 2x | próximo x |
|---|---|---|---|
| 0 | 3 | 6 | 3 − 0,6 = **2,4** |
| 1 | 2,4 | 4,8 | 2,4 − 0,48 = **1,92** |
| 2 | 1,92 | 3,84 | 1,536 → tende a 0 (o mínimo) |

Na regressão logística e nas redes neurais, o gradiente descendente minimiza a função de custo (entropia cruzada / erro quadrático).
