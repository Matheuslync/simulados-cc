---
titulo: Equações diferenciais e métodos numéricos
grupo: Matemática e IA
prioridade: media
ordem: 20
fiap:
  - Fase 6 · Cap 5 — Equações diferenciais e sistemas dinâmicos | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658038
  - Fase 6 · Cap 6 — Métodos numéricos e ponto flutuante | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658039
links:
  - Documentação do math.isclose (Python) | https://docs.python.org/pt-br/3/library/math.html#math.isclose
  - SciPy — solve_ivp para EDOs | https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
---

### Equações diferenciais (EDOs)

Uma **EDO** relaciona uma função com suas derivadas. A **ordem** é a da maior derivada. **Problema de valor inicial (PVI)** = EDO + condição inicial (ex.: `y(0) = 20`). Uma EDO de ordem n pode ser reescrita como um **sistema de n EDOs de 1ª ordem**.

Gráficos: **campo de direções** (setinhas com a inclinação em cada ponto), curvas de solução e **diagrama de fase** (uma variável contra a outra, ex.: presas × predadores).

| Modelo | Equação | Solução / comportamento |
|---|---|---|
| Decaimento radioativo / reação de 1ª ordem | `y' = −k·y` | `y = y₀·e^(−kt)`; meia-vida = `ln 2 / k` |
| Resfriamento de Newton | `T' = −k(T − Tₐ)` | `T = Tₐ + (T₀ − Tₐ)·e^(−kt)` → tende à temperatura ambiente |
| Crescimento logístico | `P' = r·P·(1 − P/K)` | cresce e estabiliza na capacidade K |
| Pêndulo (pequenas oscilações) | `θ'' + (g/L)·θ = 0` | período `2π·√(L/g)` |
| Massa-mola-amortecedor | `m·x'' + c·x' + k·x = 0` | oscila e o amortecimento c faz a amplitude cair |
| Lotka-Volterra (presa-predador) | `x' = αx − βxy`, `y' = δxy − γy` | populações oscilam defasadas |

### Métodos numéricos

**Erros:** absoluto = `|x − x̃|`; relativo = `|x − x̃| / |x|` (melhor para comparar grandezas de tamanhos diferentes).

**Ponto flutuante (IEEE 754, dupla precisão — o `float` do Python):** 64 bits = 1 de **sinal** + 11 de **expoente** (viés 1023) + 52 de **mantissa**. Precisão de máquina ε ≈ 2,2 × 10⁻¹⁶. Por isso `0.1 + 0.2 == 0.3` dá **False** → compare com `math.isclose`.

**Derivada numérica:** progressiva `(f(x+h) − f(x)) / h` tem erro O(h); **central** `(f(x+h) − f(x−h)) / 2h` tem erro O(h²), mais precisa. `numpy.gradient` usa diferenças centrais no interior.

**Iteração de ponto fixo:** reescreve `f(x) = 0` como `x = g(x)` e repete `xₖ₊₁ = g(xₖ)`. Converge perto da raiz se `|g'(x)| < 1`.

**Método de Newton:** `xₖ₊₁ = xₖ − f(xₖ) / f'(xₖ)` — converge muito rápido perto da raiz, mas falha se `f'(x) ≈ 0`. Para achar **pontos críticos**, aplica-se Newton em `f'`: `xₖ₊₁ = xₖ − f'(xₖ) / f''(xₖ)`.

**Critérios de parada:** `|xₖ₊₁ − xₖ| < tolerância`, `|f(xₖ)| < tolerância` ou número máximo de iterações.

**Método de Euler** (resolver PVI): `yₙ₊₁ = yₙ + h · f(tₙ, yₙ)`. Simples; o erro diminui com passo h menor.
