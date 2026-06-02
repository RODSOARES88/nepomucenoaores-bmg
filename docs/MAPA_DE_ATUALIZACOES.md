# Mapa de Atualizações · ecossistema BMG · regra do "tudo em conjunto"

> **Filosofia (palavras do usuário):**
> *"é um ecossistema. quando atualizo um, todos atualizam."*
>
> Toda atualização de dados operacionais (defesas, encerramentos, reembolsos, audiências, decisões, metas) **alimenta a visão estratégica da Mesa Diretora**. Mesa Diretora vive em DOIS lugares:
> 1. Site 1 · aba Mesa Diretora (visão operacional pros advogados · sem cifras de arrecadação)
> 2. Mesa Executiva NS · site dos sócios (visão completa COM financeiro)
>
> Quando atualizo qualquer dado-fonte, **propago automaticamente pros 2 sites da Mesa Diretora** + pras abas operacionais dos sites onde o dado se encaixa.

---

## 🌐 O ecossistema

```
┌─────────────────── DADOS-FONTE ───────────────────┐
│  Email Defesas semanal      Email Encerramentos    │
│  Email Reembolsos           Email Audiências        │
│  Email Snapshot Thais       Email Fechamento mensal │
│  Email Meta mensal BMG      Planilha Decisões       │
└────────────────┬───────────────────────────────────┘
                 │ propaga pra:
        ┌────────┼────────────────────────┐
        ▼        ▼                        ▼
   ┌────────┐ ┌──────────┐         ┌──────────────┐
   │ SITE 1 │ │ CENTRAL  │         │  MESA EXEC.  │
   │  BMG   │ │   DE     │         │      NS      │
   │        │ │ COMANDO  │         │ (sócios)     │
   └────┬───┘ └────┬─────┘         └──────┬───────┘
        │          │                       │
        └──┬───────┴─────────┬─────────────┘
           │                 │
           ▼                 ▼
    ┌──────────────┐   ┌──────────────┐
    │  Mesa Diret. │   │ Mesa Diret.  │
    │  (Site 1)    │   │ (Mesa NS)    │
    │  ALIMENTADA  │   │  ALIMENTADA  │
    │  por TUDO    │   │  por TUDO    │
    └──────────────┘   └──────────────┘
```

**Regra de ouro:** se um dado novo entra no ecossistema, **as 2 Mesas Diretoras DEVEM ser atualizadas** mesmo que indiretamente.

---

## 📋 Inputs e fluxo de propagação

### 1️⃣ Email/Planilha "DEFESAS APRESENTADAS" (semanal)

**Exemplo:** `Relatorio defesas Apresentadas - 19.05.2026 a 25.05.2026.xlsx`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Defesas** | Bloco "Snapshot semanal" novo · cards + pace + top colaboradoras · banner período |
| 2 | Central | **aba Financeira** | Receita defesas YTD · histórico mensal · KPIs derivados |
| 3 | Central | `DADOS.historico[mes]` | `defesas` + `defValor` · campo `defParcialAte` |
| 4 | Central | changelog | Entrada nova `data-refresh` |
| 5 | Site 1 | **aba Mesa Diretora · fala Administrativo** | Citar a evolução de defesas (sinal de capacidade) |
| 6 | Mesa NS | `FATURAMENTO_BMG.POR_MES[mes]` embedded | `defesas_qtd` + `receita_defesas` + `receita_total` |
| 7 | Mesa NS | `FATURAMENTO_BMG.AGREGADO` | `maio_receita_parcial` · `queda_receita_pct` |
| 8 | Mesa NS | **aba Mesa Diretora · fala CFO** | Mencionar receita defesas com impacto financeiro |
| 9 | Dados | `BMG-Central/faturamento-bmg.json` | `POR_MES[mes]` · sincroniza com Mesa NS |

**Checagem obrigatória ao final:** "as 2 Mesas Diretoras refletem o dado novo?"

---

### 2️⃣ Email "RESULTADO FINAL DO MÊS / FECHAMENTO" (Beatriz Duarte · dia 1-3 do mês seguinte · por produto)

**Exemplo:** `Email Beatriz · fechamento Maio por produto · 02/06`

**Propagação obrigatória (a mais ampla · 14 lugares):**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · bloco Mês fechado** | Substituir bloco em-curso por tabela detalhada por produto |
| 2 | Site 1 | **aba Ranking BMG · bloco Mês seguinte** | Status "MÊS ATIVO" + leitura estratégica à luz do fechamento |
| 3 | Site 1 | `META_INFO` | meta/realizado/dataRef |
| 4 | Site 1 | **aba Mesa Diretora · fala Administrativo** | Citar fechamento real + impacto operacional |
| 5 | Site 1 | changelog | Entrada nova |
| 6 | Central | **aba Encerramentos** | `DADOS.encerramentos[mes]` · total + receita + parcial:false |
| 7 | Central | **aba Encerramentos · banner** | "MÊS FECHADO" |
| 8 | Central | `DADOS.historico[mes]` | `enc` + `encValor` + `encFechado:true` |
| 9 | Central | `DADOS.meta{Mes}{Ano}_fechado` | Constante nova com por_produto |
| 10 | Central | **aba Financeira** | KPIs derivados recalculam · histórico atualiza |
| 11 | Central | changelog | Entrada nova |
| 12 | Mesa NS | `META_INFO` + `META_MAIO_FECHADO` | Constantes atualizadas |
| 13 | Mesa NS | **aba Mesa Diretora · fala CFO** | Citar fechamento + impacto financeiro |
| 14 | Mesa NS | `FATURAMENTO_BMG.POR_MES[mes]` + agregados | enc + receita_enc + receita_total + queda_pct |
| ★ | Dados | `BMG-Central/faturamento-bmg.json` | Sincroniza com Mesa NS |

---

### 3️⃣ Email/Planilha "ENCERRAMENTOS detalhado" (planilha com motivos · CONDENAÇÃO/IMPROCEDÊNCIA/etc)

**Exemplo:** `Encerramentos ate 31 maio.xlsx`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Encerramentos** | `DADOS.encerramentos[mes]` · motivos[] + composicao[] |
| 2 | Central | `DADOS.historico[mes]` | enc + encValor (calculado dos motivos) |
| 3 | Central | **aba Financeira** | Receita encerramentos recalcula |
| 4 | Central | changelog | Entrada nova |
| 5 | Site 1 | **aba Mesa Diretora · fala CLO/Jurídico** | Citar a composição (% improcedência vs condenação) |
| 6 | Mesa NS | `FATURAMENTO_BMG.POR_MES[mes]` embedded | improcedencias + pct_exito + receita_encerramentos |
| 7 | Mesa NS | **aba Mesa Diretora · fala CLO + CFO** | Composição jurídica + impacto receita |
| ★ | Dados | `BMG-Central/faturamento-bmg.json` | Sincroniza |

---

### 4️⃣ Email/Planilha "REEMBOLSOS pendentes"

**Exemplo:** `Relatório reembolsos pendentes até 25.05.2026.xlsx`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Reembolsos** | `DADOS.reembolsos` · statusYTD + porTipo + snapshotPendente |
| 2 | Central | **aba Financeira** | Bandeira de R$ pendente recalcula |
| 3 | Central | changelog | Entrada nova |
| 4 | Mesa NS | **aba Mesa Diretora · fala CFO** | Citar capital represado se relevante |

---

### 5️⃣ Email "META MENSAL por produto" (BMG · vésperas do mês começar)

**Exemplo:** `Email BMG · metas jun/2026 por produto`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · bloco Meta Próximo Mês** | Novo bloco com tabela por produto + barras zeradas + leitura estratégica |
| 2 | Site 1 | changelog | Entrada nova |
| 3 | Site 1 | **aba Mesa Diretora · fala Estratégico/CEO** | Citar a meta (especialmente destaque BMG) |
| 4 | Central | `DADOS.meta{Mes}{Ano}` | Constante nova |
| 5 | Central | changelog | Entrada nova |
| 6 | Mesa NS | `META_{MES}_2026` | Constante nova |
| 7 | Mesa NS | **aba Mesa Diretora · fala CEO + CFO** | Citar meta + impacto financeiro projetado |

---

### 6️⃣ Email semanal Thais (snapshot meio de mês)

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · cards + tabela + alerta** | Realizado/pace/% · adicionar linha no histórico |
| 2 | Site 1 | `META_INFO` | Atualizar |
| 3 | Site 1 | **aba Mesa Diretora · fala Administrativo/Operacional** | Citar pace atual e gap |
| 4 | Site 1 | changelog | Entrada nova |
| 5 | Central | `DADOS.encerramentos[mes]` parcial | Atualizar total se existe valor |
| 6 | Mesa NS | `META_INFO` | Atualizar |

---

### 7️⃣ Planilha "DECISÕES" semana (SharePoint pasta inteligência)

**Exemplo:** `Decisões - 19.05.2026 a 25.05.2026.xlsx`

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Site 1 | **aba Ranking BMG · bloco Snapshot semanal** | Cards de N decisões + tabelas UF×resultado + projeto×resultado |
| 2 | Site 1 | `DECISOES_FINAL` embedded | Incrementar array de decisões |
| 3 | Site 1 | `DATA[uf][causa]` | Recalcular via `recalcularDATAComDecisoesReais()` |
| 4 | Site 1 | **aba Mesa Diretora · fala CLO/Jurídico** | Citar movimentação de teses se houver |
| 5 | Site 1 | changelog | Entrada nova |
| 6 | Mesa NS | `FATURAMENTO_BMG` (se afetou improc/êxito) | Sincronizar |

---

### 8️⃣ Planilha "AUDIÊNCIAS"

**Propagação obrigatória:**

| # | Site | Onde | O que muda |
|---|---|---|---|
| 1 | Central | **aba Audiências** | `DADOS.audiencias` · virtual/presencial/híbrida + receita líquida |
| 2 | Central | **aba Financeira** | KPI Margem audiências recalcula |
| 3 | Central | `DADOS.historico[mes]` | audVir + audPre + audHib |
| 4 | Central | changelog | Entrada nova |
| 5 | Mesa NS | `FATURAMENTO_BMG.AUDIENCIAS_MES` | Atualizar valor receita audiências |

---

## ✅ Checklist universal (sempre rodar ao final)

Antes de declarar uma atualização completa:

1. **As 2 Mesas Diretoras refletem o dado?**
   - Site 1 · aba "🎯 Mesa Diretora" · uma das 5 falas dos setores foi atualizada
   - Mesa NS · aba "🎯 Mesa Diretora · BMG" · uma das 5 falas foi atualizada
2. **As constantes-fonte estão sincronizadas entre Mesa NS e BMG-Central?**
   - `FATURAMENTO_BMG` embedded na Mesa NS bate com `BMG-Central/faturamento-bmg.json`
3. **3 changelogs ganharam entrada nova?** (ou pelo menos os 2 sites afetados)
4. **JS validado** via Node VM em todos os sites alterados
5. **Encriptado** via staticrypt
6. **Push** em todos os repos afetados
7. **Tarefa marcada como completed** no TaskList

---

## 🚫 Anti-padrões a evitar

| ❌ Errado | ✅ Correto |
|---|---|
| Atualizar só a aba que ele pediu | Rodar a checklist completa do tipo de input |
| Esquecer da Mesa Diretora porque "é abstrato" | Mesa é a vitrine · sempre atualizar com fala do setor afetado |
| Atualizar Central mas não a Mesa NS porque "tem pouco tempo" | Mesa NS é onde os sócios decidem · prioridade alta |
| Atualizar HTML mas não sincronizar `BMG-Central/faturamento-bmg.json` | JSON é a fonte da verdade · sempre sincronizar |
| Não rodar Node VM antes de encriptar | Erro de JS pode quebrar o site silenciosamente · sempre validar |

---

## 📍 Como manter este mapa

- **Antes de atualizar**, abrir e fazer o checklist mental
- **Se um lugar novo afetado aparecer**, adicionar AQUI antes
- **Se um lugar não usa mais**, riscar daqui
- **Revisar mensalmente** pra eliminar entradas obsoletas

---

## 🎯 Origem dessa filosofia

Esta documentação nasceu em 02/06/2026 depois que o usuário percebeu que a aba Encerramentos da Central não foi atualizada quando o fechamento de Maio chegou — apenas porque ela não foi explicitamente pedida. A correção: ao invés de depender da memória/instinto, ter um mapa exaustivo que **garante propagação em ecossistema**.

> *"é um ecossistema. quando atualizo um, todos atualizam."*
