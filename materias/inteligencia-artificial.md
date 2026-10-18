---
titulo: Inteligência artificial e aprendizado de máquina
grupo: Matemática e IA
prioridade: media
ordem: 11
fiap:
  - Fase 1 · Cap 6 — Fundamentos de IA e aprendizado de máquina | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586184
  - Fase 5 · Cap 4 — Prompts e comandos inteligentes | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629593
  - Fase 5 · Cap 5 — Cadeias de raciocínio | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629594
  - Fase 5 · Cap 6 — Otimização de interações | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629595
links:
  - Curso intensivo de machine learning do Google (pt-br) | https://developers.google.com/machine-learning/crash-course?hl=pt-br
---

**Tipos de aprendizado**

- **Supervisionado:** dados com rótulo → **regressão** (valor numérico) ou **classificação** (categoria).
- **Não supervisionado:** sem rótulo → **clustering** (K-means), redução de dimensionalidade (PCA).
- **Por reforço:** agente aprende por tentativa e erro com **recompensas e punições**.

**Treino e avaliação:** divisão treino / validação / teste. **Risco empírico** = média da perda no conjunto de **treinamento**. **Validação cruzada** (cross-validation) = avaliar o modelo de forma estável, em várias divisões dos dados.

- **Overfitting:** decorou o treino, vai mal em dados novos → regularização (L1/L2), mais dados, validação cruzada.
- **Underfitting:** modelo simples demais.

**Redes neurais:** camadas (entrada, ocultas, saída), pesos ajustados por **backpropagation** + gradiente descendente, funções de ativação (ReLU, sigmoide). **Deep learning** = muitas camadas ocultas. O **perceptron** simples só separa dados **linearmente separáveis** → **não resolve XOR**.

**IA generativa (Fase 5)**

- **RAG:** buscar trechos relevantes em uma base de documentos e passá-los ao modelo para responder com informação atualizada/específica. Na **indexação**, os documentos são divididos em pedaços e transformados em vetores (embeddings).
- **Chain-of-Thought:** pedir o raciocínio passo a passo → melhora **raciocínio em várias etapas**.
- **Instruction tuning:** ajuste para o modelo **seguir instruções** melhor.
