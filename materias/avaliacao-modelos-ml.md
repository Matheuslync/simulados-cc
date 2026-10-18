---
titulo: Avaliação, otimização e ferramentas de ML
grupo: Matemática e IA
prioridade: media
ordem: 21
fiap:
  - Fase 5 · Cap 7 — Otimização de modelos (MSE, gradiente, regularização) | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629596
  - Fase 6 · Cap 7 — Avaliação de performance (MAE, MSE, R², AIC/BIC) | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658040
  - Fase 6 · Cap 8 — NumPy, Pandas, scikit-learn e TensorFlow | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658041
links:
  - scikit-learn — métricas de regressão | https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics
  - scikit-learn — busca de hiperparâmetros | https://scikit-learn.org/stable/modules/grid_search.html
---

**Métricas de regressão**

| Métrica | Fórmula | Leitura |
|---|---|---|
| **MAE** | média de `|y − ŷ|` | erro médio na unidade de y; menos sensível a outliers |
| **MSE** | média de `(y − ŷ)²` | **penaliza mais os erros grandes** |
| **RMSE** | `√MSE` | volta para a unidade de y |
| **R²** | variância explicada | 1 = perfeito; 0 = igual a prever a média; pode ser negativo no teste |

**Comparar modelos:** **AIC** e **BIC** medem o ajuste penalizando o número de parâmetros — **menor é melhor**. O BIC penaliza mais a complexidade.

**Hiperparâmetros** são escolhidos antes do treino (ex.: λ da regularização, profundidade de árvore); **parâmetros** são aprendidos (coeficientes).

- **Grid search:** testa **todas** as combinações de uma grade.
- **Random search:** sorteia combinações; mais eficiente quando há muitos hiperparâmetros.
- Avalie com **validação cruzada (k-fold)** para não escolher pelo acaso de uma divisão.

**Otimização:** treinar = minimizar uma função de custo (ex.: MSE) com **gradiente descendente**. **Regularização** controla overfitting: **Ridge (L2)** encolhe os coeficientes; **Lasso (L1)** pode **zerar** coeficientes e assim faz **seleção de variáveis**; Elastic Net combina os dois.

**Ferramentas**

- **NumPy:** `ndarray`, operações **vetorizadas** (sem laço), broadcasting, produto escalar/matricial (`np.dot`, `@`).
- **Pandas:** `Series` (1D) e `DataFrame` (tabela); limpeza (`dropna`, `fillna`), transformação e `groupby`.
- **Matplotlib / Seaborn:** gráficos de dispersão, histogramas, mapa de calor de correlação.
- **scikit-learn:** API `fit` / `predict` / `transform`; **Pipeline** encadeia pré-processamento e modelo.
  - **Padronização** (`StandardScaler`): média 0 e desvio 1.
  - **Normalização** (`MinMaxScaler`): escala para o intervalo 0–1.
  - **Codificação** (`OneHotEncoder`): transforma categorias em colunas 0/1.
  - Ajuste o scaler **só no treino** e aplique no teste, para não vazar informação.
- **TensorFlow:** trabalha com **tensores** (arrays de n dimensões) e treina modelos por gradiente descendente; integra com Keras.
