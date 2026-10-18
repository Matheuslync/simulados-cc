---
titulo: "Energia: eficiência, renováveis e armazenamento"
grupo: Energia e sustentabilidade
prioridade: media
ordem: 9
fiap:
  - Fase 1 · Cap 7 — Eficiência energética e indicadores | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586185
  - Fase 3 · Cap 8 — Energia solar e eólica | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609782
  - Fase 4 · Cap 7 — Armazenamento e distribuição de energia | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617913
  - Fase 6 · Cap 12 — Gerenciamento inteligente de energia | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658045
links:
  - PROCEL — Programa Nacional de Conservação de Energia Elétrica | https://www.gov.br/mme/pt-br/assuntos/secretarias/sntep/procel
---

> Questões deste tema costumam ser de **interpretação de texto**: leia o enunciado com calma e elimine as alternativas absolutas ("unicamente", "integralmente", "sempre").

**Leis da termodinâmica:** 1ª — a energia se conserva (só se transforma). 2ª — toda conversão tem perdas (entropia); nenhuma máquina tem 100% de eficiência.

| Indicador | Fórmula | Bom valor |
|---|---|---|
| Rendimento η | energia útil / energia total | perto de 1 |
| Fator de carga (FC) | demanda média / demanda máxima | perto de 1 = consumo estável |
| Fator de potência (FP) | potência ativa (P) / aparente (S) | 0,92 a 1 (abaixo: cargas indutivas → capacitores) |
| EPI | consumo real / consumo de referência | < 1 é melhor que a referência |
| **PUE** (data center) | energia total / energia de TI | 1,0 ideal; eficientes 1,2–1,4 |

ISO 50001 = sistema de gestão de energia. ODS 7 = energia limpa e acessível.

**Solar fotovoltaica:** efeito fotovoltaico em semicondutores. Células **monocristalinas** (mais eficientes, mais caras), **policristalinas** (custo-benefício) e **filme fino** (mais baratas e flexíveis, menos eficientes). **On-grid** = ligado à rede (compensação de créditos); **off-grid** = autônomo, precisa de **baterias**.

**Eólica:** potência ∝ **v³** (dobrar o vento → 8× a potência). **Limite de Betz: no máximo 59,3%** da energia do vento é aproveitável.

Solar e eólica são **intermitentes** → previsão com machine learning, supervisão SCADA, IoT e **manutenção preditiva** (antecipar falhas a partir de dados de sensores).

**Armazenamento:** baterias (íons de lítio, ~90–95% de eficiência), mecânico (hidrelétrica **reversível/bombeada**, ar comprimido, volantes de inércia), térmico (sais fundidos) e químico (**hidrogênio verde**, produzido por eletrólise com energia renovável).

**Redes inteligentes (smart grids):** sensores, automação e análise de dados que equilibram **oferta e demanda em tempo real**. Medidores inteligentes (**AMI**) medem o consumo em tempo real e comunicam nos dois sentidos. **ADMS** = sistema avançado de gestão da distribuição.
