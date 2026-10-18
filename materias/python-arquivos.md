---
titulo: "Python: arquivos (open, write, seek)"
grupo: Programação
prioridade: alta
ordem: 6
fiap:
  - Fase 5 · Cap 3 — Manipulação de arquivos e JSON | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=629592
links:
  - Tutorial oficial — leitura e escrita de arquivos | https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files
  - Documentação do módulo json | https://docs.python.org/pt-br/3/library/json.html
---

**Modos de abertura**

| Modo | O que faz |
|---|---|
| `"r"` | leitura (erro se o arquivo não existe) |
| `"w"` | escrita: **apaga** o conteúdo se existe, cria se não existe |
| `"a"` | append: escreve **no final**, mantém o conteúdo |
| `"x"` | criação exclusiva: **erro** (`FileExistsError`) se já existe |
| `"r+"` / `"w+"` | leitura + escrita (`w+` também apaga) |

**O cursor:** toda leitura e escrita acontece a partir da posição atual do cursor e o move para frente.

- `arq.write(texto)` grava e **retorna o número de caracteres gravados**. `arq.write("abc\n")` retorna 4 (o `\n` conta 1).
- Depois de escrever com `w+`, o cursor fica **no fim** → `read()` devolve `""`. Por isso usa-se `arq.seek(0)` antes de ler.
- `seek(n)` posiciona o cursor no caractere `n` (0 = início). Aceita um 2º parâmetro (referência: início, atual ou fim), mas quase sempre só se passa o 1º.
- `tell()` diz a posição atual. `read(n)` lê n caracteres.
- `readline()` lê uma linha (com o `\n`); `readlines()` devolve uma **lista** de linhas; `writelines(lista)` grava várias (não adiciona `\n`).
- `with open(...) as arq:` fecha o arquivo automaticamente.

```python
arq = open("a.txt", "w+")
arq.write("Gravando no arquivo\n")   # retorna 20
print(arq.read())                    # "" (cursor no fim)
arq.seek(0)
print(arq.read())                    # Gravando no arquivo
arq.seek(9)
print(arq.read())                    # no arquivo
arq.close()
```

**Charada "o que é, o que é":** "posiciono o cursor dentro do arquivo, ajudo a exibir parte dele, tenho dois parâmetros mas quase sempre passam só o primeiro" → **`seek`**. Não confunda com `count`, `print`, `read` ou `write`.

**count:** `texto.count("a")` e `lista.count(x)` contam ocorrências. Contar linhas: `len(arq.readlines())`.

**JSON:** `json.dumps(obj, indent=4)` → string · `json.dump(obj, arq)` → grava no arquivo · `json.loads(texto)` → lê de string · `json.load(arq)` → lê do arquivo.
