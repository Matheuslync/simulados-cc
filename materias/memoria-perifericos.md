---
titulo: Memória, periféricos e interfaces
grupo: Fundamentos
prioridade: media
ordem: 18
fiap:
  - Fase 5 · Cap 8 — Estruturas de memória | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629597
  - Fase 6 · Cap 9 — Dispositivos de comunicação e periféricos | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658042
  - Fase 3 · Cap 6 — Tipos de computadores, SO e hardware | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609780
links:
  - Hierarquia de memória na Wikipédia | https://pt.wikipedia.org/wiki/Hierarquia_de_mem%C3%B3ria
---

**Unidades:** bit (0 ou 1, menor unidade) · nibble = 4 bits · **byte = 8 bits** · word (Intel) = 16 bits. Com **n bits** dá para representar **2ⁿ** combinações — e endereçar 2ⁿ posições de memória.

Em informática os prefixos são potências de 2: **1 kB = 2¹⁰ = 1.024 bytes**, 1 MB = 2²⁰ = 1.048.576 bytes, 1 GB = 1.024 MB.

**Classificação das memórias**

| Critério | Tipos |
|---|---|
| Tecnologia | **Semicondutora** (RAM, cache, registradores, pendrive, SSD) · **magnética** (HD, fita, disquete) · **óptica** (CD, DVD, Blu-ray) |
| Volatilidade | **Volátil** perde os dados sem energia (registradores, cache, memória principal) · **não volátil** mantém (ROM, flash/SSD, HD) |
| Posição/função | registradores → cache → memória principal → armazenamento secundário |

**Pirâmide (hierarquia) de memória:** do topo para a base, **registradores → cache L1, L2, L3 → memória principal (DDR4/DDR5) → SSD/HD**. Quanto mais alto: **mais rápida, menor e mais cara** por byte. A cache L1 opera na frequência do processador e guarda o que vai ser usado em seguida.

- **RAM** = *Random Access Memory*: o tempo de acesso é o mesmo em qualquer endereço. "Memória RAM" é o apelido popular da **memória principal**.
- **ECC** (Error Correction Code): corrige erros de dados, comum em servidores.
- **Barramentos:** de **dados**, de **endereços** e de **controle**. **Largura de banda** = quantidade de dados transferida por segundo.

**Periféricos**

- Entrada: teclado, mouse, câmera, scanner. Saída: monitor, impressora. Entrada e saída: tela touch, rede.
- **Monitor OLED:** cada pixel emite a própria luz (não precisa de backlight) → preto real.
- **Impressoras:** matricial (impacto de agulhas; imprime várias vias) · jato de tinta · **laser** (toner e cilindro fotossensível) · **térmica** (papel termossensível, cupons) · plotter (grandes formatos) · 3D por filamento (FDM), **resina** (luz UV) e **sinterização** (pó fundido por laser).
- **Interfaces:** USB, rede cabeada, **Wi-Fi** (rede sem fio local), **Bluetooth** (curto alcance e baixo consumo).
- **Realidade virtual** substitui o ambiente real; **realidade aumentada** sobrepõe elementos digitais ao real.
