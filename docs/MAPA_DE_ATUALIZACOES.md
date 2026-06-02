# Mapa de Atualizações · ecossistema BMG · regra do "tudo em conjunto"

> **Filosofia (palavras do usuário):**
> *"é um ecossistema. quando atualizo um, todos atualizam."*
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
| ★ | Dados | `BMG-Central/faturamento-bmg.json` | Sincroniza com Mesa NS |

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
| 4 | Site 1 | **aba Régua BMG · leitura estratégica** | Se tese vencedora por cluster mudou, atualizar banner |
| 5 | Site 1 | **aba Carteira BMG · leitura estratégica** | Se concentração de causa raiz por UF/produto mudou, ajustar contexto |
| 6 | Site 1 | **aba Mesa Diretora · fala CLO/Jurídico** | Movimentação de teses |
| 7 | Site 1 | changelog | Entrada nova |
| 8 | Mesa NS | `FATURAMENTO_BMG` se afetou improc/êxito | Sincronizar |

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
