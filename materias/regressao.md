---
titulo: Regressão linear e logística
grupo: Matemática e IA
prioridade: media
ordem: 12
fiap:
  - Fase 3 · Cap 7 — Regressão linear simples | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609781
  - Fase 4 · Cap 5 — Regressão linear múltipla | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617911
  - Fase 4 · Cap 6 — Regressão logística | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617912
  - Fase 3 · Cap 5 — Vetores, matrizes e NumPy | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609779
links:
  - scikit-learn — modelos lineares | https://scikit-learn.org/stable/modules/linear_model.html
---

**Linear simples:** `ŷ = β₀ + β₁x`. Os coeficientes saem do **método dos mínimos quadrados**, que minimiza a **soma dos quadrados dos resíduos** (resíduo = y real − ŷ). **R²** (0 a 1) mede quanto da variação é explicada.

Interpretação: em `Ŷ = 12 + 3X`, cada unidade a mais de X aumenta Ŷ em 3; quando X = 0, Ŷ = 12.

**Linear múltipla:** várias variáveis explicativas, forma matricial `Y = Xβ + ε`. **Multicolinearidade** (explicativas correlacionadas entre si) → medida pelo **VIF**. Teste **t** avalia cada coeficiente; teste **F**, o modelo todo. **AIC/BIC** comparam modelos diferentes (menor é melhor).

**Regularização:** **Ridge (L2)** encolhe os coeficientes; **Lasso (L1)** pode zerá-los. O hiperparâmetro (λ/α) é escolhido por validação cruzada.

**Logística:** para **classificação** (sim/não). Usa a **sigmoide** `σ(z) = 1/(1+e⁻ᶻ)`, que devolve uma probabilidade entre 0 e 1; limiar típico 0,5. Trabalha com chances (odds) e log-odds. Custo: **entropia cruzada**, otimizada por gradiente descendente.

**Métricas de classificação:** acurácia; **precisão** = VP/(VP+FP); **recall** = VP/(VP+FN); F1 = média harmônica das duas; curva ROC/AUC.

**NumPy:** **vetorização** = operar no array inteiro sem laço Python (mais rápido, código em C por baixo). **Broadcasting** = operar arrays de formatos diferentes, "esticando" o menor sem copiar.
