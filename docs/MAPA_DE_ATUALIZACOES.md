# Mapa de Atualizações · ecossistema BMG · regra do "tudo em conjunto"

> **Filosofia (palavras do usuário):**
> *"é um ecossistema. quando atualizo um, todos atualizam."*
> *"o site 1 no manual, qualquer novidade eu encaminho. nas abas entradas, audiencias e visão geral eu encaminho, e nas licitações também são manuais."*

---

## 🏆 FONTE DA VERDADE OFICIAL

**Quadro Aquila** (Dashboard interno do escritório · `Atualizado DD/MM/YYYY`) é a **fonte da verdade oficial** pra encerramentos, metas mensais, % êxito por mês, % êxito por estado, base ativa, tempo médio de encerramento, entradas/saídas mensais e ativos por projeto.

**Hierarquia de fontes (quando há conflito):**
1. 🏆 **Quadro Aquila** (consolidado interno · confronta planilhas mais completas desde sempre)
2. 📧 Email Beatriz Duarte (fechamento mensal por produto · BMG oficial · bom pra detalhe por produto)
3. 📊 BI BMG Performance (snapshot oficial BMG · bom pro ranking competitivo · clusters ranqueáveis)
4. 📋 Email Thais semanal (snapshot intermediário)
5. ⚠️ Slide BMG "Meta de encerramento 2026" — **DESCARTADO em 03/06/2026** por divergir do Aquila

Sempre que receber Quadro Aquila novo, atualizar com os números dele SEM questionar e adicionar campo `fonte: "Quadro Aquila YYYY-MM-DD"` em cada registro.

---

## 🎯 Classificação das abas · MODO AUTO vs MODO MANUAL SOB DEMANDA

Antes de propagar qualquer input pelo ecossistema, lembrar dessa classificação. Algumas abas são alimentadas **automaticamente em conjunto** com fechamentos/snapshots, outras **só atualizam quando o usuário encaminha conteúdo específico delas**.

### 🔄 MODO AUTO · propagam em conjunto

Essas abas SEMPRE entram na propagação quando um dos 10 inputs chega. Cada input afeta um subconjunto delas (ver tabelas abaixo).

| Site | Aba | Por que é auto |
|---|---|---|
| **Site 1** | Plano de Inteligência | Deriva de DECISOES_FINAL · recalcula com decisões novas |
| **Site 1** | Sugestão de Modelos | Deriva de DATA · recalcula com decisões novas |
| **Site 1** | Ranking BMG | Recebe META_INFO de Thais/Beatriz/BMG |
| **Site 1** | Régua BMG | Banner leitura estratégica · todo input pode atualizar contexto. Números RGB só com Input 9 (BI BMG) |
| **Site 1** | Carteira BMG | Banner leitura estratégica · todo input pode atualizar contexto. Números só com Input 10 (Thais Entradas/Saídas) |
| **Site 1** | Inteligência de Mercado | Varredura semanal de notícias jurídicas (manual ou robô) |
| **Site 1** | Mesa Diretora | **Alimentada por TUDO** · 5 falas dos setores |
| **Site 1** | Atualizações | Changelog auto-popula data do topbar |
| **Central** | Defesas | Recebe planilha defesas semanal |
| **Central** | Encerramentos | Recebe email Beatriz + planilha detalhe |
| **Central** | Reembolsos | Recebe planilha reembolsos |
| **Central** | Financeira | KPIs derivam dos DADOS · auto-recalcula |
| **Central** | **Visão Geral** | **AUTO** · É a vista resumida dos números das outras abas (palavras do usuário: *"a visão geral na central tem que corresponder aos números específicos de cada aba"*). KPIs derivam de DADOS.historico[mesAtual]. Sempre que atualizo Defesas/Encerramentos/Audiências, a Visão Geral reflete em auto. |
| **Central** | Atualizações | Changelog · auto |
| **Mesa NS** | Mesa Diretora · BMG | Espelho da Mesa Site 1 + financeiro pros sócios |

### 🤝 MODO MANUAL SOB DEMANDA · só atualiza quando o usuário encaminha

**Estas abas NÃO entram na propagação automática dos 10 inputs.** Quando o usuário envia algo específico delas, eu atualizo SÓ aquela aba e suas dependências diretas.

| Site | Aba | Como atualizar |
|---|---|---|
| **Site 1** | Manual da Equipe | Quando usuário encaminha novidade/procedimento novo |
| **Central** | Entradas | Quando usuário encaminha planilha/email de entradas |
| **Central** | Audiências | Quando usuário encaminha planilha/email de audiências |
| **Mesa NS** | Mesa de Licitações | Quando usuário encaminha conteúdo de licitação |
| **Mesa NS** | Visão Consolidada | Quando usuário pede |
| **Radar Licitações** | Tudo | Manual sob demanda |
| **Radar Análise** | Tudo | Manual sob demanda |

**Regra:** se o usuário NÃO mencionou explicitamente essas abas, eu NÃO mexo nelas mesmo durante propagação de fechamentos mensais.

---
>
> Toda atualização de dados operacionais (defesas, encerramentos, reembolsos, audiências, decisões, metas) **alimenta a visão estratégica da Mesa Diretora E também os painéis estruturais (Régua BMG e Carteira BMG)**.
>
> Mesa Diretora vive em DOIS lugares:
> 1. Site 1 · aba Mesa Diretora (visão operacional pros advogados · sem cifras de arrecadação)
> 2. Mesa Executiva NS · site dos sócios (visão completa COM financeiro)
>
> **Régua BMG** e **Carteira BMG** são abas do Site 1 (e também aparecem na Mesa NS) que mostram o contexto estrutural — quanto temos em estoque, performance por cluster Região×Projeto, etc. Elas precisam de pelo menos uma das duas coisas:
> - **Atualização DIRETA** quando vem o snapshot upstream (BI BMG ou planilha Entradas/Saídas)
> - **Atualização da LEITURA ESTRATÉGICA** (banner/insights/contexto) quando dado operacional novo mudou a interpretação

---

## 🌐 O ecossistema completo

```
┌─────────── DADOS-FONTE (8 tipos) ──────────────┐
│  Defesas semanais      Encerramentos detalhados │
│  Reembolsos            Audiências                │
│  Snapshot Thais        Fechamento mensal         │
│  Meta mensal           Planilha Decisões         │
│                                                  │
│  + 2 snapshots estruturais:                      │
│  Screenshot BI BMG · Entradas/Saídas Processos   │
└────────────────┬────────────────────────────────┘
                 │ propaga pra:
        ┌────────┼─────────────────────┐
        ▼        ▼                     ▼
   ┌────────┐ ┌──────────┐      ┌──────────────┐
   │ SITE 1 │ │ CENTRAL  │      │  MESA EXEC.  │
   │  BMG   │ │   DE     │      │      NS      │
   │        │ │ COMANDO  │      │ (sócios)     │
   └───┬────┘ └────┬─────┘      └──────┬───────┘
       │           │                    │
       │ ┌─────────────────────┐        │
       ├─┤ aba Mesa Diretora   │────────┤
       │ └─────────────────────┘        │
       │ ┌─────────────────────┐        │
       ├─┤ aba Régua BMG       │        │
       │ └─────────────────────┘        │
       │ ┌─────────────────────┐        │
       └─┤ aba Carteira BMG    │────────┘
         └─────────────────────┘
                ▲           ▲
         atualizam só    atualizam só
         com upstream    com upstream
         específico      específico
         (BI BMG)        (Plan. Entradas/Saídas)
```

**Regra de ouro:** TODO dado novo afeta pelo menos UM dos 3 destinos:
1. As 2 Mesas Diretoras (fala dos setores)
2. Régua BMG (números OU leitura estratégica)
3. Carteira BMG (números OU leitura estratégica)

---

## 📋 Inputs e fluxo de propagação

### 1️⃣ Email/Planilha "DEFESAS APRESENTADAS" (semanal)

**Exemplo:** `Relatorio defesas Apresentadas - 19.05.2026 a 25.05.2026.xlsx`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Defesas** | Bloco "Snapshot semanal" novo + banner + período |
| 2 | Central | **aba Financeira** | Receita defesas YTD · KPIs derivados |
| 3 | Central | `DADOS.historico[mes]` | `defesas` + `defValor` |
| 4 | Central | changelog | Entrada nova |
| 5 | Site 1 | **aba Mesa Diretora · fala Administrativo** | Citar evolução de defesas (sinal de capacidade) |
| 6 | Site 1 | **aba Carteira BMG · leitura estratégica** | Se entradas estão acelerando/freando, atualizar contexto do painel "estoque vs absorção" |
| 7 | Mesa NS | `FATURAMENTO_BMG.POR_MES[mes]` embedded | defesas_qtd + receita_defesas + receita_total |
| 8 | Mesa NS | `FATURAMENTO_BMG.AGREGADO` | maio_receita · queda_pct |
| 9 | Mesa NS | **aba Mesa Diretora · fala CFO** | Receita defesas com impacto financeiro |
| ★ | Dados | `BMG-Central/faturamento-bmg.json` | Sincroniza com Mesa NS |

---

### 2️⃣ Email "RESULTADO FINAL DO MÊS / FECHAMENTO" (Beatriz · dia 1-3 do mês seguinte · por produto)

**Exemplo:** `Email Beatriz · fechamento Maio por produto · 02/06`

**Propagação obrigatória (a mais ampla):**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · bloco Mês fechado** | Substituir bloco em-curso por tabela por produto |
| 2 | Site 1 | **aba Ranking BMG · bloco Mês seguinte** | Status "MÊS ATIVO" + leitura estratégica |
| 3 | Site 1 | `META_INFO` | meta/realizado/dataRef |
| 4 | Site 1 | **aba Mesa Diretora · fala Administrativo** | Citar fechamento real |
| 5 | Site 1 | **aba Régua BMG · leitura estratégica** | Se o fechamento revelou cluster específico em queda, ajustar banner/contexto. Ex: "Cartão Modalidade fechou em 42% — produto onde temos 49,6% de êxito histórico" |
| 6 | Site 1 | **aba Carteira BMG · ajustar AGREGADO** | `AGREGADO.encerradas` += encerramentos do mês · `em_curso` -= idem (só se for material e estiver claro o dia do snapshot original) |
| 7 | Site 1 | changelog | Entrada nova |
| 8 | Central | **aba Encerramentos** | `DADOS.encerramentos[mes]` total/receita/parcial |
| 9 | Central | **aba Encerramentos · banner** | "MÊS FECHADO" + texto |
| 10 | Central | **aba Encerramentos · headers/footers/fontes** | Trocar "Abril/26" por mês mais recente fechado |
| 11 | Central | `DADOS.historico[mes]` | enc + encValor + encFechado:true |
| 12 | Central | `DADOS.meta{Mes}{Ano}_fechado` | Constante nova com por_produto |
| 13 | Central | **aba Financeira** | KPIs recalcula automaticamente |
| 14 | Central | changelog | Entrada nova |
| 15 | Mesa NS | `META_INFO` + `META_MAIO_FECHADO` | Constantes atualizadas |
| 16 | Mesa NS | **aba Mesa Diretora · fala CFO** | Fechamento + impacto financeiro |
| 17 | Mesa NS | **aba Régua BMG · leitura estratégica** | Idem Site 1 |
| 18 | Mesa NS | **aba Carteira BMG · AGREGADO** | Idem Site 1 |
| 19 | Mesa NS | `FATURAMENTO_BMG.POR_MES[mes]` + agregados | enc + receita_enc + receita_total + queda |
| 20 | **Mesa NS** | **`data/estrategia-ativa.json` ⚠️ CRÍTICO + AUTOMATIZÁVEL** | **decisoes_resumidas + bandeiras + sessao.data + meta_mes_ativo + kpis_resumo. Este JSON alimenta o widget azul 'Decisões Mesa Diretora' no topo do Site 1 e Central via fetch · TODOS os 3 sites pegam atualização automática em ~1-2min após push.<br><br>🤖 **Não fazer manual!** Existe wrapper local: `C:\Users\Rodrigo\Documents\BMG-Central\sync-estrategia.bat`. Roda `_gera_estrategia.py v2` que detecta cenário (fechamento_recente / em_curso / apenas_fechado) automaticamente a partir do `faturamento-bmg.json` (campo `METAS_MENSAIS`) + carteira + decisões, gera o JSON com bandeiras e decisoes adaptativas, faz git add/commit/push da Mesa NS. 1 comando = ecossistema sincronizado.** |
| ★ | Dados | `BMG-Central/faturamento-bmg.json` | Sincroniza com Mesa NS · **deve ter `METAS_MENSAIS` atualizado por mês** (status=fechado com realizados ou status=ativo com só meta) |
| ★★ | Local | `BMG-Central/_gera_estrategia.py v2` | Script Python adaptativo · lê faturamento + carteira + decisões · gera estrategia-ativa.json com cenário detectado |
| ★★★ | Local | `BMG-Central/sync-estrategia.bat` | Wrapper de 1 comando · roda script + commit + push da Mesa NS |

---

### 3️⃣ Planilha "ENCERRAMENTOS detalhada" (com motivos · CONDENAÇÃO/IMPROCEDÊNCIA/etc)

**Exemplo:** `Encerramentos ate 31 maio.xlsx`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Encerramentos** | `DADOS.encerramentos[mes]` · motivos[] + composicao[] |
| 2 | Central | `DADOS.historico[mes]` | enc + encValor (calculado dos motivos) |
| 3 | Central | **aba Financeira** | Receita encerramentos recalcula |
| 4 | Central | changelog | Entrada nova |
| 5 | Site 1 | **aba Mesa Diretora · fala CLO/Jurídico** | Citar composição % improcedência vs condenação |
| 6 | Site 1 | **aba Régua BMG · leitura estratégica** | Se % improc por cluster mudou materialmente, atualizar banner do cluster |
| 7 | Mesa NS | `FATURAMENTO_BMG.POR_MES[mes]` embedded | improc + pct_exito + receita_enc |
| 8 | Mesa NS | **aba Mesa Diretora · fala CLO + CFO** | Composição + impacto receita |
| ★ | Dados | `BMG-Central/faturamento-bmg.json` | Sincroniza |

---

### 4️⃣ Email/Planilha "REEMBOLSOS pendentes"

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Reembolsos** | `DADOS.reembolsos` · statusYTD + porTipo + snapshotPendente |
| 2 | Central | **aba Financeira** | Bandeira R$ pendente recalcula |
| 3 | Central | changelog | Entrada nova |
| 4 | Mesa NS | **aba Mesa Diretora · fala CFO** | Capital represado se relevante |

---

### 5️⃣ Email "META MENSAL por produto" (BMG · vésperas do mês)

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · bloco Meta Próximo Mês** | Bloco completo com tabela por produto + barras zeradas + leitura estratégica |
| 2 | Site 1 | **aba Mesa Diretora · fala Estratégico/CEO** | Citar meta (destaque BMG) |
| 3 | Site 1 | **aba Régua BMG · leitura estratégica** | Se BMG destacar cluster específico (ex: Cartão Modalidade), atualizar contexto do cluster correspondente |
| 4 | Site 1 | changelog | Entrada nova |
| 5 | Central | `DADOS.meta{Mes}{Ano}` | Constante nova |
| 6 | Central | changelog | Entrada nova |
| 7 | Mesa NS | `META_{MES}_2026` | Constante nova |
| 8 | Mesa NS | **aba Mesa Diretora · fala CEO + CFO** | Meta + impacto projetado |

---

### 6️⃣ Email semanal Thais (snapshot meio de mês)

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · cards + tabela + alerta** | Realizado/pace/% · linha no histórico |
| 2 | Site 1 | `META_INFO` | Atualizar |
| 3 | Site 1 | **aba Mesa Diretora · fala Adm/Operacional** | Pace atual + gap |
| 4 | Site 1 | changelog | Entrada nova |
| 5 | Central | `DADOS.encerramentos[mes]` parcial | Atualizar total parcial |
| 6 | Mesa NS | `META_INFO` | Atualizar |

---

### 7️⃣ Planilha "DECISÕES" semana (SharePoint pasta inteligência)

**Exemplo:** `Decisões - 19.05.2026 a 25.05.2026.xlsx`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · bloco Snapshot semanal** | Cards + tabelas UF×resultado + projeto×resultado |
| 2 | Site 1 | `DECISOES_FINAL` embedded | Incrementar array |
| 3 | Site 1 | `DATA[uf][causa]` | Recalcular via `recalcularDATAComDecisoesReais()` |
| 4 | Site 1 | **aba Ranking BMG · bloco Matriz UF × Projeto (probabilidade)** | Recalcular % favorável de cada cruzamento (script `_probabilidade_uf_projeto.py` em BMG-Central · gera `_probabilidade_uf_projeto.json` · atualizar cells HTML do heatmap + TOP 5 + BOTTOM 5) |
| 5 | Site 1 | **aba Régua BMG · leitura estratégica** | Se tese vencedora por cluster mudou, atualizar banner |
| 6 | Site 1 | **aba Carteira BMG · leitura estratégica** | Se concentração de causa raiz por UF/produto mudou, ajustar contexto |
| 7 | Site 1 | **aba Mesa Diretora · fala CLO/Jurídico** | Movimentação de teses |
| 8 | Site 1 | changelog | Entrada nova |
| 9 | Mesa NS | **Matriz UF × Projeto (espelho)** | Sincronizar HTML do heatmap com Site 1 |
| 10 | Mesa NS | `FATURAMENTO_BMG` se afetou improc/êxito | Sincronizar |

---

### 8️⃣ Planilha "AUDIÊNCIAS"

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Audiências** | `DADOS.audiencias` · virtual/presencial/híbrida + receita líquida |
| 2 | Central | **aba Financeira** | KPI Margem audiências recalcula |
| 3 | Central | `DADOS.historico[mes]` | audVir + audPre + audHib |
| 4 | Central | changelog | Entrada nova |
| 5 | Mesa NS | `FATURAMENTO_BMG.AUDIENCIAS_MES` | Atualizar receita audiências |

---

### 9️⃣ 🆕 Screenshot do BI BMG (dashboard interno do banco · cluster Região × Projeto)

**Exemplo:** screenshot do "BI Performance" enviado pelo gestor BMG com tabela completa dos 11 clusters atualizados.

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Régua BMG · tabela principal** | `RGB_DATA` atualizada com 11 clusters · enc/pctEx/metaEx/tkt/metaTkt |
| 2 | Site 1 | **aba Régua BMG · banner data snapshot** | Atualizar "BI BMG · snapshot DD/MM" |
| 3 | Site 1 | **aba Régua BMG · cards de resumo** | Recalcula dinamicamente (n bateu meta · n não bateu · etc) |
| 4 | Site 1 | **aba Mesa Diretora · fala CEO/Estratégico** | Citar clusters em status crítico (não bateu meta de êxito) |
| 5 | Site 1 | changelog | Entrada nova |
| 6 | Mesa NS | `RGB_DATA_2026` | Sincronizar com Site 1 |
| 7 | Mesa NS | `METAS_ANUAIS_BMG` | Atualizar meta anual se vier no screenshot |
| 8 | Mesa NS | **aba Mesa Diretora · fala CEO** | Idem Site 1 |

---

### 1️⃣1️⃣ 🆕 Snapshot Dashboard Aquila (escritório interno · mensal · FONTE DA VERDADE)

**Exemplo:** screenshots da tela Aquila com Visão Geral · Base ativa por UF · Ativos por projeto · Fluxo entrada/saída mensal · Detalhamento mês fechado · Ranking êxito por estado.

**Frequência:** ideal mensal · Aquila atualizado normalmente no dia 14 do mês.

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | `faturamento-bmg.json → QUADRO_AQUILA` | Substituir TODAS as 6 subseções (visao_geral, base_ativa_por_uf_pct, ativos_por_projeto, fluxo_mensal_entrada_saida, ULTIMO_MES_fechado_detalhamento, exitos_por_estado_ranking) + bumpar `data_atualizacao` |
| 2 | Central | `faturamento-bmg.json → POR_MES` | Para cada mês que Aquila atualizou: substituir `encerramentos` e `pct_exito` + adicionar `fonte_oficial: "Quadro Aquila YYYY-MM-DD"` e `meta_aquila` |
| 3 | Central | `faturamento-bmg.json → METAS_ANUAIS_BMG` | Se Aquila trouxe metas atualizadas, substituir |
| 4 | Site 1 | **aba Ranking BMG · bloco Pulso Operacional Aquila** | 4 cards (sobrecarga, velocity YTD, pra zerar, tempo médio) + tabela Velocity mensal + tabela Base por UF + Top projetos + Ranking êxito + Detalhamento mês mágico + 3 decisões fechamento |
| 5 | Site 1 | **aba Ranking BMG · bloco Meta Anual** | Atualizar última linha (mês novo fechado) + déficit acumulado |
| 6 | Site 1 | **aba Mesa Diretora · fala CFO/Administrativo** | Atualizar déficit + ~R$ receita perdida |
| 7 | Site 1 | **aba Mesa Diretora · fala CEO/Estratégico** | Atualizar narrativa segundo mês mágico ou ruim |
| 8 | Site 1 | changelog | Entrada nova |
| 9 | Mesa NS | **seção colapsável Pulso Aquila** | Replicar mudanças do Site 1 |
| 10 | Mesa NS | **seção colapsável Matriz UF × Projeto** | Verificar se concentração mudou |
| 11 | Mesa NS | `FATURAMENTO_BMG` se afetou improc/êxito | Sincronizar |

**Cuidado:** Aquila é fonte da verdade · qualquer divergência com Beatriz, BMG ou Thais, **Aquila ganha** (decisão do usuário 03/06/2026).

---

### 🔟 🆕 Planilha "Entradas e Saidas Processos" (Gestor Jurídico BMG · estoque atual da carteira)

**Exemplo:** `Entradas e Saidas Processos.xlsx` (mensal · Thais ou similar)

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Carteira BMG · KPIs principais** | `CARTEIRA_BMG.AGREGADO` · total + em_curso + encerradas + improc + condenação + taxa_exito + SLA |
| 2 | Site 1 | **aba Carteira BMG · POR_PROJETO** | Atualizar 7 projetos (modalidade · fraude · adv_agressor · etc) |
| 3 | Site 1 | **aba Carteira BMG · POR_UF** | Atualizar 7 UFs (MG · SP · RS · SC · PR · RJ · ES) |
| 4 | Site 1 | **aba Carteira BMG · POR_PRODUTO** | Atualizar produtos (cartao · cartao_beneficio · consignado · etc) |
| 5 | Site 1 | **aba Carteira BMG · MATRIZ_PROJ_PROD** | Cruzamento projeto × produto |
| 6 | Site 1 | **aba Carteira BMG · banner data snapshot** | "Gestor Jurídico BMG · snapshot DD/MM" |
| 7 | Site 1 | **aba Mesa Diretora · fala CEO + Risco/CRO** | Cluster pior em curso (exposição material) |
| 8 | Site 1 | changelog | Entrada nova |
| 9 | Mesa NS | `CARTEIRA_BMG` | Sincronizar com Site 1 (idênticos) |
| 10 | Mesa NS | **aba Mesa Diretora · fala CEO + CRO** | Idem Site 1 |

---

## 📐 Convenções da Régua e Carteira (regra de "snapshot congelado")

**Régua BMG (`RGB_DATA`):**
- É uma FOTO do BI BMG no momento que o gestor mandar
- Atualização DIRETA dos números → só com novo screenshot (Input 9)
- Mas a LEITURA ESTRATÉGICA (banner/contexto/insight) deve ser ajustada quando dado operacional novo mudar a interpretação
- Ex: Cartão Modalidade fechou em 42% → banner da Régua pode dizer "Cluster onde fechamos abaixo da meta apesar de ter 49,6% de êxito histórico"

**Carteira BMG (`CARTEIRA_BMG`):**
- É uma FOTO da planilha "Entradas e Saidas Processos" no momento da Thais mandar
- Atualização DIRETA dos números → só com nova planilha (Input 10)
- Mas a LEITURA ESTRATÉGICA pode ser ajustada com dados operacionais novos
- Ex: 283 encerramentos no Maio → banner pode dizer "AGREGADO.em_curso provavelmente caiu ~283 desde o snapshot · estimativa atualizada: ~6.767"

---

## ✅ Checklist universal (sempre rodar ao final)

1. **As 2 Mesas Diretoras refletem o dado?**
   - Site 1 · uma das 5 falas dos setores foi atualizada
   - Mesa NS · idem
2. **As constantes-fonte estão sincronizadas?**
   - `FATURAMENTO_BMG` na Mesa NS bate com `BMG-Central/faturamento-bmg.json`
   - `RGB_DATA_2026` na Mesa NS bate com `RGB_DATA` no Site 1
   - `CARTEIRA_BMG` na Mesa NS bate com `CARTEIRA_BMG` no Site 1
3. **Régua BMG e Carteira BMG têm a leitura estratégica atualizada?** (Mesmo que os números não mudem, o banner/contexto deve refletir o que aprendemos com o dado novo)
4. **3 changelogs ganharam entrada nova?**
5. **JS validado** via Node VM em todos os sites alterados
6. **Encriptado** via staticrypt
7. **Push** em todos os repos afetados
8. **Tarefa marcada como completed** no TaskList

---

## 🚫 Anti-padrões a evitar

| ❌ Errado | ✅ Correto |
|---|---|
| Atualizar só a aba que ele pediu | Rodar a checklist completa do tipo de input |
| Esquecer da Mesa Diretora | Mesa é a vitrine · sempre atualizar com fala do setor afetado |
| Esquecer da Régua/Carteira porque "são snapshots fixos" | Mesmo que os números não mudem, atualizar a LEITURA ESTRATÉGICA com o contexto novo |
| Atualizar HTML mas não sincronizar JSON | JSON é fonte da verdade · sempre sincronizar |
| Não rodar Node VM antes de encriptar | Erro de JS quebra silenciosamente · sempre validar |

---

## 🎯 Origem dessa filosofia

Esta documentação nasceu em 02/06/2026 depois que o usuário percebeu que (a) a aba Encerramentos da Central não foi atualizada quando o fechamento de Maio chegou, e (b) a aba Régua/Carteira também devia receber a leitura estratégica nova.

A solução: documentar exaustivamente, garantir que NADA cai entre as cadeiras.

> *"é um ecossistema. quando atualizo um, todos atualizam."*
> *"e tudo tem atualizar tambem a aba regua e carteira do bmg."*

---

## 📍 Como manter este mapa

- **Antes de cada update**, abrir este arquivo e fazer o checklist
- **Se descobrir um novo lugar afetado**, adicionar AQUI antes de atualizar
- **Se um lugar não usa mais um dado**, riscar daqui
- **Revisar mensalmente** pra eliminar entradas obsoletas
