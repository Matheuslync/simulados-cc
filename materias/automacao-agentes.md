---
titulo: Automação de fluxos e agentes (n8n)
grupo: Matemática e IA
prioridade: media
ordem: 23
fiap:
  - Fase 6 · Cap 13 — Assistentes virtuais, n8n, webhooks e agentes com LLM | https://on.fiap.com.br/mod/conteudoshtml/view.php?id=658046
links:
  - Documentação do n8n | https://docs.n8n.io/
---

**Automação de fluxos (workflow automation):** fluxos pré-definidos, disparados por **gatilhos**, executam ações sem intervenção manual (enviar e-mail, atualizar planilha, chamar API). Reduz retrabalho e erro humano.

**No n8n, cada bloco é um nó (node):**

- **Trigger nodes** (gatilhos): iniciam o fluxo — agendamento (**schedule/cron**), **webhook** (escuta uma chamada externa), e-mail recebido, evento de banco de dados.
- **Action nodes:** fazem algo — buscar ou transformar dados, chamar APIs, enviar mensagens.
- Os dados passam de nó em nó como **itens em JSON**.
- Pode rodar na nuvem do n8n ou em servidor próprio (**self-hosted**).

**Nós importantes**

| Nó | Função |
|---|---|
| **Webhook** | recebe uma requisição HTTP de fora e **inicia** o workflow |
| **HTTP Request** | o workflow **chama** uma API externa |
| **OpenAI** | envia um prompt a um modelo e recebe a resposta |
| **AI Agent** | agente com LLM que decide quais **ferramentas** usar, com memória e instruções |

**Boas práticas e limites:** guardar credenciais com segurança, tratar erros e tentativas, validar a saída do LLM (pode **alucinar**), controlar custo de tokens e não dar ao agente mais permissões do que o necessário.

Exemplos de uso: coleta agendada de dados da web, sincronização entre CRM e ERP, atendimento com assistente virtual.
