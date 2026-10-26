# Simulados CC — Fases 1 a 6

Resumos, links e um banco de questões **colaborativo** para estudar e fazer simulados de Ciência da Computação da FIAP (1º ano), fases 1 a 6.

**Site:** https://matheuslync.github.io/simulados-cc/

O site tem:

- **Roteiro:** as matérias em ordem de prioridade de estudo, com um checklist.
- **Matérias:** resumo de cada matéria, os capítulos do FIAP ON onde ela aparece e links para se aprofundar.
- **Treinar:** uma questão por vez, com correção e explicação na hora, filtrando por matéria ou fase.
- **Simulado:** 10 a 40 questões sorteadas, com mais peso para as matérias de prioridade alta; correção só no final.
- **Erros:** o que você errou, para refazer.
- **Histórico:** os simulados que você fez, com nota, evolução, acerto por matéria e a correção completa de cada um.

Seu progresso fica salvo no navegador. Não há login nem servidor.

## Como estudar

1. **Leia o resumo** da matéria (aba Matérias do site ou pasta [`materias/`](materias/)). Comece pelas de prioridade alta.
2. **Abra o capítulo no FIAP ON** pelo link da matéria e releia o **fast test** do fim do capítulo. Ele não pode ser refeito, mas depois de respondido mostra a alternativa correta e a explicação; tente responder de cabeça antes de olhar.
3. **Revise o quiz da fase** no FIAP ON depois que a fase fecha: na página do quiz, abra a revisão da sua tentativa e releia as que errou.
4. **Treine no site** as questões da matéria, com correção na hora.
5. **Faça um simulado** nas fases que quer cobrir e refaça o que errou na aba Erros.

Os fast tests e quizzes ficam no portal: este repositório só aponta para eles, não copia.

> **Atualização das questões:** o banco é alimentado depois que cada fase termina. Matérias da fase em andamento só ganham questões após o encerramento dela.

Acha que falta um assunto ou que uma prioridade está errada? Abra uma issue ou edite os arquivos em `materias/`.

## Matérias

Tabela gerada automaticamente a partir de [`materias/`](materias/) pelo `scripts/build.py`. Os links do FIAP ON só abrem para quem tem login.

<!-- materias:inicio -->
| Matéria | Fases | Prioridade | Questões | Capítulos FIAP | Para se aprofundar |
|---|---|---|---|---|---|
| [Heap (heap binário)](materias/heap.md) | 2 · 6 | 🔴 alta | 7 | [Fase 6 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658037)<br>[Fase 2 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604027) | [VisuAlgo — animação de heap binário](https://visualgo.net/en/heap)<br>[Documentação do heapq (Python)](https://docs.python.org/3/library/heapq.html) |
| [Trie (árvore de prefixos)](materias/trie.md) | 6 | 🔴 alta | 6 | [Fase 6 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658037) | [Trie na Wikipédia](https://pt.wikipedia.org/wiki/Trie)<br>[Visualização interativa de trie (USFCA)](https://www.cs.usfca.edu/~galles/visualization/Trie.html) |
| [Tabela hash](materias/tabela-hash.md) | 3 | 🔴 alta | 7 | [Fase 3 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609778) | [VisuAlgo — tabela hash (sondagem linear, quadrática, encadeamento)](https://visualgo.net/en/hashtable)<br>[Tabela de dispersão na Wikipédia](https://pt.wikipedia.org/wiki/Tabela_de_dispers%C3%A3o) |
| [Árvores binárias (BST, AVL, Red-Black)](materias/arvores-binarias.md) | 2 · 3 | 🔴 alta | 7 | [Fase 3 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609778)<br>[Fase 2 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604027) | [VisuAlgo — BST e AVL](https://visualgo.net/en/bst)<br>[Visualização de Red-Black Tree (USFCA)](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html) |
| [Mapa de Karnaugh](materias/mapa-de-karnaugh.md) | 3 · 5 · 6 | 🔴 alta | 11 | [Fase 6 · Cap 2](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658035)<br>[Fase 3 · Cap 2](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609776)<br>[Fase 5 · Cap 2](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629591) | [Mapa de Karnaugh na Wikipédia](https://pt.wikipedia.org/wiki/Mapa_de_Karnaugh) |
| [Python: arquivos (open, write, seek)](materias/python-arquivos.md) | 5 | 🔴 alta | 12 | [Fase 5 · Cap 3](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629592) | [Tutorial oficial — leitura e escrita de arquivos](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files)<br>[Documentação do módulo json](https://docs.python.org/pt-br/3/library/json.html) |
| [Python: fundamentos e leitura de código](materias/python-fundamentos.md) | 1 · 2 · 3 · 4 | 🔴 alta | 15 | [Fase 1 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586182)<br>[Fase 1 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586183)<br>[Fase 2 · Cap 3](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604025)<br>[Fase 3 · Cap 3](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609777)<br>[Fase 4 · Cap 2](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617908) | [Tutorial oficial de Python (pt-br)](https://docs.python.org/pt-br/3/tutorial/index.html)<br>[Python Tutor — veja o código executar passo a passo](https://pythontutor.com/visualize.html) |
| [Derivada e gradiente descendente](materias/gradiente-descendente.md) | 2 · 4 | 🔴 alta | 8 | [Fase 4 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617910)<br>[Fase 4 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617912)<br>[Fase 2 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604028) | [Gradient descent na Wikipédia (inglês)](https://en.wikipedia.org/wiki/Gradient_descent)<br>[Khan Academy — derivadas](https://pt.khanacademy.org/math/calculus-1) |
| [Energia: eficiência, renováveis e armazenamento](materias/energia.md) | 1 · 3 · 4 · 5 · 6 | 🟡 média | 10 | [Fase 1 · Cap 7](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586185)<br>[Fase 3 · Cap 8](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609782)<br>[Fase 4 · Cap 7](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617913)<br>[Fase 5 · Cap 10](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629599)<br>[Fase 6 · Cap 12](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658045) | [PROCEL — Programa Nacional de Conservação de Energia Elétrica](https://www.gov.br/mme/pt-br/assuntos/secretarias/sntep/procel) |
| [Sustentabilidade, ESG e TI verde](materias/sustentabilidade.md) | 1 · 2 · 4 | 🟡 média | 4 | [Fase 1 · Cap 8](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586186)<br>[Fase 2 · Cap 8](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604030)<br>[Fase 4 · Cap 8](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617914) | [Objetivos de Desenvolvimento Sustentável (ONU Brasil)](https://brasil.un.org/pt-br/sdgs) |
| [Inteligência artificial e aprendizado de máquina](materias/inteligencia-artificial.md) | 1 · 5 | 🟡 média | 3 | [Fase 1 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586184)<br>[Fase 5 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629593)<br>[Fase 5 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629594)<br>[Fase 5 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629595) | [Curso intensivo de machine learning do Google (pt-br)](https://developers.google.com/machine-learning/crash-course?hl=pt-br) |
| [Regressão linear e logística](materias/regressao.md) | 3 · 4 | 🟡 média | 3 | [Fase 3 · Cap 7](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609781)<br>[Fase 4 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617911)<br>[Fase 4 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617912)<br>[Fase 3 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609779) | [scikit-learn — modelos lineares](https://scikit-learn.org/stable/modules/linear_model.html) |
| [Estruturas lineares: vetor, pilha, fila, lista](materias/estruturas-lineares.md) | 2 · 4 | 🟡 média | 2 | [Fase 2 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604026)<br>[Fase 4 · Cap 2](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617908) | [VisuAlgo — lista, pilha e fila](https://visualgo.net/en/list) |
| [Complexidade, busca e ordenação](materias/complexidade-ordenacao.md) | 2 · 6 | 🟡 média | 6 | [Fase 2 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604027)<br>[Fase 6 · Cap 3](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658036) | [VisuAlgo — algoritmos de ordenação animados](https://visualgo.net/en/sorting)<br>[Big-O Cheat Sheet](https://www.bigocheatsheet.com/) |
| [Grafos: BFS, DFS e Dijkstra](materias/grafos.md) | 4 | 🟡 média | 2 | [Fase 4 · Cap 3](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=617909) | [VisuAlgo — BFS e DFS](https://visualgo.net/en/dfsbfs)<br>[VisuAlgo — caminho mínimo (Dijkstra)](https://visualgo.net/en/sssp) |
| [Portas lógicas e bases numéricas](materias/portas-logicas-bases.md) | 1 · 2 · 6 | 🟡 média | 3 | [Fase 1 · Cap 3](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586181)<br>[Fase 2 · Cap 2](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604024)<br>[Fase 6 · Cap 10](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658043) | [Simulador de circuitos lógicos (Logic.ly)](https://logic.ly/demo/) |
| [Memória, periféricos e interfaces](materias/memoria-perifericos.md) | 3 · 5 · 6 | 🟡 média | 5 | [Fase 5 · Cap 8](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629597)<br>[Fase 6 · Cap 9](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658042)<br>[Fase 3 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609780) | [Hierarquia de memória na Wikipédia](https://pt.wikipedia.org/wiki/Hierarquia_de_mem%C3%B3ria) |
| [Eletricidade e circuitos](materias/eletricidade-circuitos.md) | 6 | 🟡 média | 5 | [Fase 6 · Cap 11](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658044) | [PhET — simulador de circuitos (Universidade do Colorado)](https://phet.colorado.edu/pt_BR/simulations/circuit-construction-kit-dc) |
| [Equações diferenciais e métodos numéricos](materias/metodos-numericos-edos.md) | 6 | 🟡 média | 5 | [Fase 6 · Cap 5](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658038)<br>[Fase 6 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658039) | [Documentação do math.isclose (Python)](https://docs.python.org/pt-br/3/library/math.html#math.isclose)<br>[SciPy — solve_ivp para EDOs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) |
| [Avaliação, otimização e ferramentas de ML](materias/avaliacao-modelos-ml.md) | 5 · 6 | 🟡 média | 5 | [Fase 5 · Cap 7](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629596)<br>[Fase 6 · Cap 7](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658040)<br>[Fase 6 · Cap 8](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658041) | [scikit-learn — métricas de regressão](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)<br>[scikit-learn — busca de hiperparâmetros](https://scikit-learn.org/stable/modules/grid_search.html) |
| [Ética, diversidade e cultura](materias/etica-diversidade.md) | 5 · 6 | 🟡 média | 4 | [Fase 5 · Cap 9](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629598)<br>[Fase 6 · Cap 14](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658047) | [Lei 10.639/2003 (Planalto)](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.639.htm) |
| [Automação de fluxos e agentes (n8n)](materias/automacao-agentes.md) | 6 | 🟡 média | 4 | [Fase 6 · Cap 13](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658046) | [Documentação do n8n](https://docs.n8n.io/) |
| [Linguagem C](materias/linguagem-c.md) | 2 · 6 | 🟡 média | 4 | [Fase 2 · Cap 4](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604026)<br>[Fase 6 · Cap 3](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658036) | [Referência da linguagem C (cppreference)](https://en.cppreference.com/w/c) |
| [História da computação, hardware e SO](materias/historia-hardware.md) | 1 · 2 · 3 | ⚪ baixa | 3 | [Fase 1 · Cap 2](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=586180)<br>[Fase 2 · Cap 7](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=604029)<br>[Fase 3 · Cap 6](https://on.fiap.com.br/mod/conteudoshtml/view.php?id=609780) | [Computer History Museum — linha do tempo](https://www.computerhistory.org/timeline/) |
<!-- materias:fim -->

## Como usar no seu computador

Precisa só do Python 3.9 ou mais novo, sem instalar nada.

```bash
git clone https://github.com/Matheuslync/simulados-cc.git
cd simulados-cc
python3 scripts/build.py      # valida tudo e gera site/dados.js
open site/index.html          # macOS; no Linux: xdg-open, no Windows: start
```

## Seu banco de questões

Tem questões suas em um arquivo `.json`? No site, na aba **Roteiro**, use **Importar arquivo .json**. Elas passam a aparecer em Treinar, Simulado e Erros junto com as do site, com a etiqueta e o filtro **Pessoal (local)**, inclusive com o guia de revisão nos erros.

- As questões importadas ficam **só no navegador de quem importou** (armazenamento local). Não são enviadas para o GitHub nem para ninguém, e outras pessoas que abrem o site não as veem.
- Dá para importar vários arquivos; questões com o mesmo `id` são substituídas. O botão **Remover questões importadas** apaga tudo.
- Em outro navegador ou aparelho, é preciso importar de novo. Em janela anônima, nada fica salvo.
- Questões com problema (matéria inexistente, resposta inválida…) são ignoradas e listadas depois da importação.

Formato: uma lista de questões no mesmo formato das questões do repositório, mais o campo `materia` (o nome de um arquivo de [`materias/`](materias/), sem `.md`):

```json
[
  {
    "materia": "python-arquivos",
    "pergunta": "Qual método posiciona o cursor em um ponto do arquivo?",
    "alternativas": ["read", "write", "seek", "count"],
    "resposta": "C",
    "explicacao": "seek(n) leva o cursor para a posição n.",
    "fase": 5,
    "origem": "Minhas anotações"
  }
]
```

| Campo | Obrigatório | Descrição |
|---|---|---|
| `materia` | sim | Id da matéria, ex.: `heap`, `mapa-de-karnaugh`, `python-arquivos` |
| `pergunta`, `alternativas`, `resposta` | sim | Como nas questões do repositório; `resposta` pode ser letra (`"C"`) ou índice (`2`) |
| `explicacao`, `codigo`, `fase` | não | Como nas questões do repositório |
| `origem` | não | Etiqueta exibida na questão (ex.: "Minhas anotações") |
| `id` | não | Identificador para substituir a questão ao reimportar |

Quem roda o site no próprio computador também pode colocar esses arquivos na pasta `privado/` (ignorada pelo git): o `python3 scripts/build.py` os inclui no `site/dados.js` local.

## Contribuindo

Contribuições são muito bem-vindas, principalmente **questões novas** das matérias de prioridade alta. Cada questão é um arquivo JSON pequeno em `questoes/<matéria>/`, e dá para criar direto pelo navegador no GitHub. Quem não usa git pode [sugerir uma questão por formulário](../../issues/new?template=nova-questao.yml).

Leia o [guia de contribuição](CONTRIBUTING.md) para o formato, as regras e como testar.

## Estrutura

```
materias/          um resumo por matéria (Markdown com cabeçalho de metadados)
questoes/<materia>/ uma questão por arquivo .json
scripts/build.py   valida tudo e gera site/dados.js (e a tabela de matérias deste README)
site/index.html    o site (HTML + JS puro)
.github/           validação de pull requests, publicação no GitHub Pages e formulário de questão
```

## Publicando o site

O workflow `.github/workflows/pages.yml` gera e publica o site a cada push na `main` (fonte do GitHub Pages: **GitHub Actions**). Em um fork, ative em **Settings → Pages → Build and deployment → GitHub Actions**.

## Aviso

Material feito por alunos para alunos, para estudo. **Não é um material oficial da FIAP** e pode conter erros; na dúvida, confira no capítulo correspondente do FIAP ON. Os resumos e questões deste repositório são de autoria dos contribuidores.

## Licença

- Código (`scripts/`, `site/`, `.github/`): [MIT](LICENSE).
- Resumos e questões (`materias/`, `questoes/`): [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR) — pode copiar e adaptar citando a fonte e mantendo a mesma licença.
