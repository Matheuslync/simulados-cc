#!/usr/bin/env python3
"""Valida as matérias e questões e gera site/dados.js.

Uso:
  python3 scripts/build.py           # valida e gera o site
  python3 scripts/build.py --check   # só valida (usado no CI)

Sem dependências externas: só a biblioteca padrão do Python 3.9+.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MATERIAS = RAIZ / "materias"
QUESTOES = RAIZ / "questoes"
PRIVADO = RAIZ / "privado"
SAIDA = RAIZ / "site" / "dados.js"

PRIORIDADES = {"alta": 3, "media": 2, "baixa": 1}
CAMPOS_QUESTAO = {"pergunta", "alternativas", "resposta", "explicacao", "codigo", "linguagem", "fase", "autor", "fonte"}
LETRAS = "ABCDEF"

erros = []
avisos = []


def erro(arquivo, msg):
    erros.append(f"{arquivo.relative_to(RAIZ)}: {msg}")


def aviso(arquivo, msg):
    avisos.append(f"{arquivo.relative_to(RAIZ)}: {msg}")


def ler_frontmatter(arquivo):
    """Lê o cabeçalho entre '---' (subconjunto simples de YAML: chave: valor e listas '- item')."""
    texto = arquivo.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", texto, re.S)
    if not m:
        erro(arquivo, "faltou o cabeçalho entre linhas '---' no início do arquivo")
        return {}, texto
    meta, chave = {}, None
    for n, linha in enumerate(m.group(1).splitlines(), 2):
        if not linha.strip():
            continue
        item = re.match(r"^\s+-\s+(.*)$", linha)
        par = re.match(r"^([a-z_]+):\s*(.*)$", linha)
        if item and chave:
            meta.setdefault(chave, []).append(item.group(1).strip())
        elif par:
            chave, valor = par.group(1), par.group(2).strip()
            if valor:
                meta[chave] = valor.strip('"').strip("'")
        else:
            erro(arquivo, f"linha {n} do cabeçalho não entendida: {linha!r}")
    return meta, m.group(2).strip()


def ler_links(arquivo, itens, campo):
    links = []
    for item in itens or []:
        if " | " not in item:
            erro(arquivo, f"em '{campo}', use o formato 'Texto | https://...': {item!r}")
            continue
        texto, url = item.rsplit(" | ", 1)
        if not re.match(r"^https?://\S+$", url.strip()):
            erro(arquivo, f"em '{campo}', URL inválida: {url!r}")
            continue
        links.append({"texto": texto.strip(), "url": url.strip()})
    return links


def ler_fases(arquivo, valor, fiap):
    """Fases da matéria: campo 'fases: 1, 2, 6' ou, se ausente, deduzidas de 'Fase N' nos links do FIAP."""
    if valor:
        try:
            fases = sorted({int(x) for x in str(valor).replace(" ", "").split(",") if x})
        except ValueError:
            erro(arquivo, f"fases deve ser uma lista de números separados por vírgula (recebido: {valor!r})")
            return []
    else:
        fases = sorted({int(n) for l in fiap for n in re.findall(r"Fase (\d+)", l["texto"])})
    if not fases:
        aviso(arquivo, "sem fase: adicione 'fases: 1, 2' ou links 'Fase N · Cap M' em fiap")
    for f in fases:
        if not 1 <= f <= 7:
            erro(arquivo, f"fase fora do intervalo 1 a 7: {f}")
    return fases


def carregar_materias():
    materias = []
    for arquivo in sorted(MATERIAS.glob("*.md")):
        mid = arquivo.stem
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", mid):
            erro(arquivo, "o nome do arquivo deve ser em minúsculas, sem acentos, com hífens (ex.: tabela-hash.md)")
        meta, corpo = ler_frontmatter(arquivo)
        for campo in ("titulo", "grupo", "prioridade"):
            if not meta.get(campo):
                erro(arquivo, f"campo obrigatório ausente no cabeçalho: {campo}")
        prio = meta.get("prioridade", "media")
        if prio not in PRIORIDADES:
            erro(arquivo, f"prioridade deve ser alta, media ou baixa (recebido: {prio!r})")
        if len(corpo) < 80:
            aviso(arquivo, "resumo muito curto")
        fiap = ler_links(arquivo, meta.get("fiap"), "fiap")
        fases = ler_fases(arquivo, meta.get("fases"), fiap)
        materias.append({
            "id": mid,
            "titulo": meta.get("titulo", mid),
            "grupo": meta.get("grupo", "Outros"),
            "prioridade": PRIORIDADES.get(prio, 2),
            "ordem": int(meta.get("ordem", 99)) if str(meta.get("ordem", "99")).isdigit() else 99,
            "fases": fases,
            "fiap": fiap,
            "links": ler_links(arquivo, meta.get("links"), "links"),
            "md": corpo,
        })
    return materias


def validar_questao(arquivo, q, ids_materias, origem):
    if not isinstance(q, dict):
        erro(arquivo, "a questão deve ser um objeto JSON { ... }")
        return None
    desconhecidos = set(q) - CAMPOS_QUESTAO - {"materia", "origem", "id"}
    if desconhecidos:
        erro(arquivo, f"campos desconhecidos: {', '.join(sorted(desconhecidos))}")
    for campo in ("pergunta", "alternativas", "resposta", "explicacao"):
        if campo not in q or q[campo] in ("", None, []):
            erro(arquivo, f"campo obrigatório ausente ou vazio: {campo}")
            return None
    if not isinstance(q["pergunta"], str) or len(q["pergunta"].strip()) < 5:
        erro(arquivo, "pergunta muito curta")
    alts = q["alternativas"]
    if not isinstance(alts, list) or not 2 <= len(alts) <= 6 or not all(isinstance(a, str) and a.strip() for a in alts):
        erro(arquivo, "alternativas deve ser uma lista de 2 a 6 textos não vazios")
        return None
    if len({a.strip().lower() for a in alts}) != len(alts):
        erro(arquivo, "há alternativas repetidas")
    resp = str(q["resposta"]).strip().upper()
    if resp not in LETRAS[: len(alts)]:
        erro(arquivo, f"resposta deve ser uma letra entre A e {LETRAS[len(alts) - 1]} (recebido: {q['resposta']!r})")
        return None
    if "fase" in q and q["fase"] not in range(1, 8):
        erro(arquivo, "fase deve ser um número de 1 a 7")
    codigo = q.get("codigo", "")
    if codigo and q.get("linguagem", "python") == "python":
        try:
            compile(codigo, str(arquivo), "exec")
        except SyntaxError as e:
            erro(arquivo, f"o código Python não compila (linha {e.lineno}): {e.msg}")
    materia = q.get("materia")
    if materia not in ids_materias:
        erro(arquivo, f"matéria {materia!r} não existe em materias/")
    return {
        "id": q.get("id") or str(arquivo.relative_to(RAIZ).with_suffix("")),
        "materia": materia,
        "pergunta": q["pergunta"].strip(),
        "codigo": codigo,
        "alternativas": [a.strip() for a in alts],
        "resposta": LETRAS.index(resp),
        "explicacao": q["explicacao"].strip(),
        "fase": q.get("fase"),
        "autor": q.get("autor", ""),
        "fonte": origem,
        "origem": q.get("origem", ""),
    }


def carregar_questoes(ids_materias):
    questoes = []
    for arquivo in sorted(QUESTOES.rglob("*")):
        if arquivo.is_dir() or arquivo.name.startswith(("_", ".")):
            continue
        if arquivo.suffix != ".json":
            erro(arquivo, "questões devem ser arquivos .json")
            continue
        partes = arquivo.relative_to(QUESTOES).parts
        if len(partes) != 2:
            erro(arquivo, "coloque a questão em questoes/<materia>/<arquivo>.json")
            continue
        try:
            q = json.loads(arquivo.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            erro(arquivo, f"JSON inválido (linha {e.lineno}, coluna {e.colno}): {e.msg}")
            continue
        if isinstance(q, dict):
            if q.get("materia", partes[0]) != partes[0]:
                erro(arquivo, f"o campo 'materia' ({q['materia']!r}) não bate com a pasta ({partes[0]!r})")
            q["materia"] = partes[0]
        v = validar_questao(arquivo, q, ids_materias, "comunidade")
        if v:
            questoes.append(v)
    return questoes


def carregar_privadas(ids_materias):
    """Questões pessoais guardadas só na sua máquina (pasta privado/, ignorada pelo git)."""
    questoes = []
    for arquivo in sorted(PRIVADO.glob("*.json")):
        try:
            lista = json.loads(arquivo.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            erro(arquivo, f"JSON inválido: {e.msg}")
            continue
        for i, q in enumerate(lista):
            q.setdefault("id", f"privado/{arquivo.stem}/{i}")
            v = validar_questao(arquivo, q, ids_materias, "pessoal")
            if v:
                questoes.append(v)
    return questoes


def checar_duplicadas(questoes):
    vistos = {}
    for q in questoes:
        chave = re.sub(r"\W+", " ", q["pergunta"].lower()).strip() + "|" + "|".join(sorted(a.lower() for a in q["alternativas"]))
        if chave in vistos:
            erros.append(f"{q['id']}: questão duplicada de {vistos[chave]}")
        vistos[chave] = q["id"]


def url_repo():
    url = os.environ.get("REPO_URL", "")
    if not url:
        try:
            url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=RAIZ, capture_output=True, text=True).stdout.strip()
        except OSError:
            url = ""
    url = re.sub(r"^git@github\.com:", "https://github.com/", url)
    return re.sub(r"\.git$", "", url)


README = RAIZ / "README.md"
MARCA_INI, MARCA_FIM = "<!-- materias:inicio -->", "<!-- materias:fim -->"


def tabela_readme(materias, por_materia):
    """Tabela de matérias do README, gerada a partir de materias/*.md."""
    rotulo = {3: "🔴 alta", 2: "🟡 média", 1: "⚪ baixa"}
    linhas = ["| Matéria | Fases | Prioridade | Questões | Capítulos FIAP | Para se aprofundar |", "|---|---|---|---|---|---|"]
    for m in sorted(materias, key=lambda m: (-m["prioridade"], m["ordem"])):
        fiap = "<br>".join(f"[{l['texto'].split(' — ')[0]}]({l['url']})" for l in m["fiap"]) or "—"
        ext = "<br>".join(f"[{l['texto']}]({l['url']})" for l in m["links"]) or "—"
        linhas.append(f"| [{m['titulo']}](materias/{m['id']}.md) | {' · '.join(map(str, m['fases'])) or '—'} | {rotulo[m['prioridade']]} | {por_materia[m['id']]} | {fiap} | {ext} |")
    return "\n".join(linhas)


def atualizar_readme(materias, por_materia, escrever):
    if not README.exists():
        return
    texto = README.read_text(encoding="utf-8")
    if MARCA_INI not in texto or MARCA_FIM not in texto:
        return
    ini, fim = texto.index(MARCA_INI) + len(MARCA_INI), texto.index(MARCA_FIM)
    novo = texto[:ini] + "\n" + tabela_readme(materias, por_materia) + "\n" + texto[fim:]
    if novo == texto:
        return
    if escrever:
        README.write_text(novo, encoding="utf-8")
        print("✓ tabela de matérias do README atualizada")
    else:
        print("aviso: a tabela de matérias do README está desatualizada; rode python3 scripts/build.py para atualizar")


def main():
    so_checar = "--check" in sys.argv
    materias = carregar_materias()
    ids = {m["id"] for m in materias}
    questoes = carregar_questoes(ids)
    checar_duplicadas(questoes)
    privadas = [] if so_checar else carregar_privadas(ids)

    for a in avisos:
        print("aviso:", a)
    if erros:
        print(f"\n{len(erros)} problema(s) encontrado(s):\n")
        for e in erros:
            print("  ✗", e)
        sys.exit(1)

    por_materia = {m["id"]: 0 for m in materias}
    for q in questoes:
        por_materia[q["materia"]] += 1
    print(f"✓ {len(materias)} matérias e {len(questoes)} questões da comunidade válidas")
    for mid, n in sorted(por_materia.items(), key=lambda x: x[1]):
        print(f"   {n:3d}  {mid}")
    atualizar_readme(materias, por_materia, escrever=not so_checar)
    if so_checar:
        return

    fases_materia = {m["id"]: m["fases"] for m in materias}
    for q in questoes + privadas:
        q["fases"] = [q["fase"]] if q["fase"] else fases_materia.get(q["materia"], [])

    dados = {
        "materias": sorted(materias, key=lambda m: (m["ordem"], m["titulo"])),
        "questoes": questoes + privadas,
        "repo": url_repo(),
        "gerado_em": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }
    js = "window.DADOS = " + json.dumps(dados, ensure_ascii=False).replace("</", "<\\/") + ";\n"
    SAIDA.write_text(js, encoding="utf-8")
    extra = f" + {len(privadas)} pessoais locais (privado/)" if privadas else ""
    print(f"✓ gerado {SAIDA.relative_to(RAIZ)}{extra}")


if __name__ == "__main__":
    main()
