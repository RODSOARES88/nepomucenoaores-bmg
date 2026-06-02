# Setup da API Anthropic para varredura automática de notícias jurídicas

Este passo a passo cria uma **API key da Anthropic** (Claude API) que o GitHub Actions usa toda segunda 9h pra fazer a varredura de notícias jurídicas, atualizar o Site 1 e gerar o briefing.

**Quem precisa fazer:** você (não precisa ser admin de nada — é uma conta pessoal Anthropic).

**Quanto tempo:** ~5 minutos.

**Custo:** **~R$ 5-10/mês** estimado (4 varreduras × ~R$ 1-2,50 cada). Você adiciona crédito (mínimo US$ 5 / ~R$ 28) e a API consome conforme uso.

---

## Passo 1 · Criar conta Anthropic (se ainda não tem)

1. Acesse https://console.anthropic.com
2. Faça login com Google ou crie conta com email
3. Aceite os termos

Se já tem conta (do Claude.ai), use a mesma — é a mesma conta.

---

## Passo 2 · Adicionar crédito

A API Anthropic é **pré-paga**. Você precisa adicionar crédito antes de usar.

1. No console, vá em **Settings → Billing → Plans**
2. Clique em **"Buy credits"**
3. Adicione o mínimo: **US$ 5** (~R$ 28). Dura ~5-10 meses de varreduras semanais.
4. Adicione cartão de crédito ou Pix

Recomendação: ativar **"Auto reload"** com limite de US$ 20/mês pra não correr o risco de a varredura falhar por falta de crédito.

---

## Passo 3 · Gerar a API key

1. No console, vá em **Settings → API Keys**
2. Clique em **"+ Create Key"**
3. Preencha:
   - **Name:** `bmg-sites-varredura-semanal`
   - **Workspace:** deixa "Default"
4. Clique em **"Create Key"**
5. **IMPORTANTE:** copie a key inteira (começa com `sk-ant-...`). Ela aparece UMA vez. Se você sair sem copiar, precisa apagar e criar outra.

---

## Passo 4 · Adicionar o secret no GitHub

1. Acesse o repo do Site 1: https://github.com/RODSOARES88/nepomucenoaores-bmg
2. Vá em **Settings → Secrets and variables → Actions**
3. Clique em **"New repository secret"**
4. Preencha:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Secret:** cole a key do Passo 3 (que começa com `sk-ant-...`)
5. Clique em **"Add secret"**

Também precisa do secret da senha do StatiCrypt (se ainda não estiver criado):

6. Repita: **"New repository secret"**
7. Preencha:
   - **Name:** `STATICRYPT_PASSWORD`
   - **Secret:** `Cafe_Mineiro_Codex_99`
8. Clique em **"Add secret"**

---

## Passo 5 · Testar manualmente

1. No repo do GitHub, vá em **Actions**
2. No menu lateral, clique no workflow **"Varredura semanal de notícias jurídicas"**
3. Clique em **"Run workflow"** → branch `main` → **"Run workflow"**

Em ~2-3 minutos o workflow termina. Se deu certo:
- O Site 1 está atualizado com as notícias novas
- Uma **Issue** foi aberta no GitHub com o título "📰 Briefing semanal AAAA-MM-DD"
- A issue contém: notícias novas + lista de modelos sugeridos pra revisão

Se deu erro de **autenticação**: provavelmente esqueceu de adicionar o secret `ANTHROPIC_API_KEY` ou colocou errado.

Se deu erro de **crédito insuficiente**: precisa adicionar mais saldo no console Anthropic.

---

## Manutenção

- **Sem manutenção rotineira.** A API key não expira automaticamente.
- Você só precisa revisitar quando:
  - **Crédito acaba** (~ a cada 5-10 meses) → adicionar mais
  - **Quiser pausar** → desligar o workflow em Actions → workflow → ⋯ → Disable
  - **Quiser mudar fontes/temas** → editar `scripts/varredura_noticias.py` (eu posso te ajudar)

---

## Troubleshooting

| Sintoma | Causa | Solução |
|---|---|---|
| `401 Unauthorized` na API | Key inválida ou faltando | Verificar secret `ANTHROPIC_API_KEY` no GitHub |
| `403 Forbidden` da API | Sem créditos | Adicionar saldo no console Anthropic |
| Workflow roda mas nada muda no site | Nenhuma notícia nova detectada | Esperado — a varredura abre issue só se houver novidade relevante |
| Issue do briefing não foi criada | Permissão do workflow ao repo | Settings → Actions → General → Workflow permissions → marcar "Read and write" |
| Site 1 ficou quebrado depois da varredura | JS inválido produzido pelo Claude | Rollback: `git revert HEAD` no main · me avisa pra ajustar o prompt |

---

## Privacidade

- A API key dá acesso à sua conta de cobrança Anthropic, mas **só** isso. Não tem acesso ao Claude.ai (sua conta de chat) — são separadas.
- O conteúdo das varreduras (busca + prompt) **não é usado para treinar** modelos Anthropic (política padrão da API enterprise).
- Você pode rotacionar a key a qualquer momento (Settings → API Keys → ⋯ → Delete) e gerar uma nova.

---

## Custo real (transparência)

Estimativa baseada na varredura que fiz manualmente hoje:
- Input tokens: ~8.000 (lista de 39 modelos + prompt + contexto)
- Output tokens: ~2.500 (5 notícias estruturadas + briefing)
- Web search: ~5 buscas

Com Claude Sonnet 4.7 (recomendado pro custo-benefício):
- Input: $3/MTok × 8 = $0,024
- Output: $15/MTok × 2,5 = $0,038
- Web search: $10/1k buscas × 5 = $0,05
- **Total: ~$0,11/varredura ≈ R$ 0,60**
- **4 segundas/mês: ~R$ 2,40-3,00/mês**

Estimativa de R$ 8/mês original foi conservadora. Real provavelmente R$ 3-5/mês.
