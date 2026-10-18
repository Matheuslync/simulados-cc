# Guia de contribuição

Obrigado por ajudar! Este repositório é feito por alunos para alunos de Ciência da Computação da FIAP. O foco é a **prova das fases 1 a 6**, principalmente as matérias que mais caem: heap, trie, tabela hash, árvores binárias, mapa de Karnaugh, Python (arquivos e leitura de código) e gradiente descendente.

Você pode contribuir de três jeitos, do mais fácil ao mais completo:

1. **Sugerir uma questão sem usar git:** abra uma issue com o formulário [Sugerir questão](../../issues/new?template=nova-questao.yml). Alguém do projeto transforma em arquivo.
2. **Adicionar questões:** um arquivo `.json` por questão em `questoes/<matéria>/`.
3. **Melhorar um resumo ou adicionar links:** edite o arquivo da matéria em `materias/`.

Pelo GitHub dá para fazer 2 e 3 direto no navegador: abra a pasta, clique em **Add file → Create new file** (ou no lápis para editar) e o GitHub cria o fork e o pull request para você.

## Regra mais importante: direitos autorais

**Não envie conteúdo copiado do FIAP ON**: texto dos capítulos, Fast tests, Quizzes, atividades ou provas. Esse material pertence à FIAP e não pode ser redistribuído em um repositório público.

Pode (e deve):

- escrever questões com suas palavras sobre os mesmos assuntos;
- criar variações (outros números, outros códigos, outras situações);
- resumir conceitos com suas palavras;
- colocar **links** para os capítulos do FIAP ON (quem tem login abre).

Se quiser treinar com as questões oficiais, guarde-as na pasta `privado/` da sua máquina (ela é ignorada pelo git). Veja o README.

## Adicionando uma questão

Crie um arquivo em `questoes/<matéria>/<nome>.json`. A pasta precisa ter o mesmo nome de um arquivo em `materias/` (ex.: `questoes/heap/` ↔ `materias/heap.md`). O nome do arquivo é livre; use algo descritivo ou um número (`heapify-down.json`, `012.json`). Um arquivo por questão evita conflitos entre contribuições.

```json
{
  "pergunta": "Qual a complexidade de remover o topo de um heap com n elementos?",
  "alternativas": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
  "resposta": "B",
  "explicacao": "Troca a raiz pelo último elemento e desce (heapify-down) pela altura da árvore: O(log n).",
  "fase": 6,
  "autor": "seu-usuario-do-github"
}
```

| Campo | Obrigatório | Descrição |
|---|---|---|
| `pergunta` | sim | Enunciado. Use `\n` para quebrar linha. |
| `alternativas` | sim | Lista com 2 a 6 textos, sem repetição. |
| `resposta` | sim | Letra da correta (`"A"` a `"F"`). |
| `explicacao` | sim | Por que a correta é a correta. Uma ou duas frases. |
| `codigo` | não | Trecho de código mostrado abaixo do enunciado. Use `\n` para as linhas. |
| `linguagem` | não | `"python"` (padrão) ou outra. Código Python é compilado na validação para pegar erro de sintaxe. |
| `fase` | não | Número da fase (1 a 7) em que o assunto aparece. |
| `autor` | não | Seu usuário do GitHub, para aparecer no crédito. |

Dicas para uma boa questão:

- **Uma ideia por questão.** Se a pergunta testa duas coisas, divida em duas.
- **Alternativas plausíveis.** Os erros devem ser os erros que um aluno comete de verdade (ex.: esquecer que o `\n` conta no `write`).
- **Questões com código:** rode o código antes e confira a saída. É o tipo de questão que mais aparece na prova.
- **Explique o porquê**, não só "a correta é B".

O arquivo `questoes/_modelo.json.txt` tem um modelo para copiar.

### Escrevendo código dentro do JSON

O JSON não aceita quebra de linha literal dentro de texto. Use `\n` para quebrar linha, `\"` para aspas e `\\n` quando o código em si tiver um `\n`:

```json
"codigo": "arq = open(\"t.txt\", \"w\")\nn = arq.write(\"Marte\\n\")\nprint(n)"
```

Esse código aparece no site assim:

```python
arq = open("t.txt", "w")
n = arq.write("Marte\n")
print(n)
```

## Editando ou criando uma matéria

Cada matéria é um arquivo Markdown em `materias/` com um cabeçalho e o resumo:

```markdown
---
titulo: Heap (heap binário)
grupo: Estrutura de dados
prioridade: alta
ordem: 1
fiap:
  - Fase 6 · Cap 4 — Estruturas avançadas: heaps e tries | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658037
links:
  - VisuAlgo — animação de heap binário | https://visualgo.net/en/heap
---

Resumo em Markdown: listas, **negrito**, `código`, tabelas e blocos de código.
```

| Campo | Descrição |
|---|---|
| `titulo` | Nome exibido no site. Se tiver `:`, coloque entre aspas. |
| `grupo` | Agrupa as matérias na aba Matérias (ex.: `Estrutura de dados`, `Python`). |
| `prioridade` | `alta`, `media` ou `baixa`. Define a ordem do roteiro e o peso no simulado. Use `alta` só para o que comprovadamente cai na prova. |
| `ordem` | Número para ordenar as matérias. |
| `fiap` | Capítulos do FIAP ON onde o assunto aparece, no formato `Texto | URL`. |
| `links` | Materiais externos gratuitos (documentação, visualizações, vídeos), no formato `Texto | URL`. |

O nome do arquivo vira o identificador da matéria: minúsculas, sem acento, com hífen (`tabela-hash.md`). Ao criar uma matéria nova, crie também a pasta `questoes/<mesmo-nome>/` e adicione a matéria à lista do formulário em `.github/ISSUE_TEMPLATE/nova-questao.yml`.

Resumos bons para este projeto são **curtos e focados na prova**: definição, tabela de complexidade, um exemplo resolvido e as pegadinhas que costumam cair.

## Testando antes de enviar

Precisa só do Python 3.9 ou mais novo, sem instalar nada.

```bash
python3 scripts/build.py --check   # valida tudo (o mesmo que roda no pull request)
python3 scripts/build.py           # valida e gera site/dados.js
```

Depois abra `site/index.html` no navegador para ver sua questão no site.

A validação aponta o arquivo e o problema, por exemplo:

```
✗ questoes/heap/012.json: resposta deve ser uma letra entre A e D (recebido: 'E')
```

## Pull request

- Um pull request pode ter várias questões, de preferência da mesma matéria.
- O checklist do pull request pede para confirmar autoria e que o código foi executado.
- A validação roda automaticamente. Quando o pull request entra na `main`, o site é publicado de novo sozinho.

## Viu um erro?

Na aba Treinar, cada questão tem um botão **Corrigir** que abre o arquivo dela no GitHub. Se preferir, abra uma issue descrevendo o problema.
