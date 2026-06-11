# 📋 Manual de Atualização · Ecossistema BMG

> **Propósito:** Pra cada planilha que chega, saber EXATAMENTE o que mexer em cada um dos 3 sites · zero esquecimento.
>
> **Atualizado:** 2026-06-11 · v1.0 (consolidado depois que descobrimos que era fácil esquecer header/footer ao atualizar dados)

---

## 🧭 Filosofia & arquitetura

```
            Planilhas (SharePoint / Downloads)
                       ↓
            ┌──────────┴──────────┐
            │                     │
        Site 1                 Central          ← dados operacionais (SEM R$ escritório)
     (advogados)          (gestão administrativa)
            │                     │
            └──────────┬──────────┘
                       ↓ (sintetiza · cruza · decisão $$)
                  Mesa NS                       ← camada decisória (COM R$)
                  (sócios)
```

**Fonte da verdade oficial (hierarquia):**
1. 🏆 Quadro Aquila (interno)
2. 📧 Email Beatriz Duarte (BMG oficial fechamento)
3. 📊 BI BMG Performance
4. 📋 Email Thais semanal
5. ⚠️ Slide BMG metas → DESCARTADO 03/06

**Regra de visibilidade financeira:** Site 1 e Central NÃO exibem receita do escritório (honorários · bônus · ROI em R$). Mesa NS pode tudo. Detalhe em [regra_visibilidade_financeira](../../../../.claude/projects/C--Users-Rodrigo/memory/regra_visibilidade_financeira.md).

---

## 🗺 Padrão dos 5 pontos por aba

Sempre que dados de uma aba mudam, conferir os **5 pontos**:

| # | Ponto | Como localizar |
|---|---|---|
| 1 | **Estrutura JS** (`DADOS.X` / `const X`) | Onde o dado vive · sem isso o render quebra |
| 2 | **Função render** (`renderX()`) | Lê estrutura JS e injeta no DOM |
| 3 | **HTML estático** (textos no `<section>`) | Header, badges, descrições · **ESCAPA fácil** |
| 4 | **Headers/footers fonte** (`source-header`, `card-footer-src`) | Mostram qual fonte · ficam desatualizados |
| 5 | **Texto dentro do render** (strings em `template literal` do JS) | Ex: "Abril e Maio ainda zerados" · também ESCAPA |

---

## 1️⃣ Inventário · Site 1

Decryptado em `Documents/Site1-BMG/decrypted/index.html`. Estruturas globais e funções render por aba:

| Aba | data-tab | Estrutura JS | Função render | HTML específico |
|---|---|---|---|---|
| Plano de Inteligência | `inteligencia` | `DATA`, `DECISOES_FINAL` | `renderTable()` + `renderCharts()` (linhas 5633/5662) | seletores UF + Causa |
| Inteligência de Mercado | `mercado` | `NEWS`, `BMG_WINS`, `DECISOES_FINAL.ALERTAS` | `renderNews()`, `renderBmgWins()`, `renderAlertasGlobais()` (3675/3777/3746) | filtros · cards |
| Sugestão de Modelos | `modelos` | `MODELS`, `MODELOS_INDEX`, `DECISOES_FINAL` | `renderModelos()` (4358) | seletor UF×Causa · bloco Matriz Modelos×Clusters · Saúde · Plano Produção |
| Manual da Equipe | `manual` | `TEAM_CONTENT` (5271) | `renderTeam(team)` (5547) | 6 botões equipe |
| Fluxos das Equipes | `fluxo` | `FLOW_DATA` (4638) | render inline | gráficos fluxo |
| Ranking BMG | `ranking` | `RGB_DATA`, `RANKING_FORMULA`, `METAS_ANUAIS_BMG`, `DECISOES_FINAL`, `QUADRO_AQUILA` | `renderMetaMensal()` (5913) + blocos estáticos (Snapshot Semanal, Matriz UF×Projeto, Pulso Aquila, Ondas de Entrada, Ranking BMG Como Subir, Gargalos UF) | **TUDO estático** — mexe muito aqui quando dados Aquila/Matriz mudam |
| Régua BMG | `regua-bmg` | `RGB_DATA` | `renderReguaBMG()` (6008) | banner leitura estratégica |
| Carteira BMG | `carteira` | `CARTEIRA_BMG`, `QUADRO_AQUILA` | `renderCarteira()` (5804) | 4 cards · tabela comparativa Aquila vs Real · aging · concentração |
| Mesa Diretora | `mesa` | `DECISOES_FINAL`, `CARTEIRA_BMG` | `renderMesaDiretora()` (6855) | 5 falas dos setores |
| Atualizações | `atualizacoes` | `CHANGELOG_S1` (5395+) | `renderChangelogS1()` (6522) | entrada nova por mudança |

**Estruturas globais a manter sincronizadas:** `DATA`, `DECISOES_FINAL`, `BMG_WINS`, `MODELS`, `MODELOS_INDEX`, `RGB_DATA`, `RANKING_FORMULA`, `METAS_ANUAIS_BMG`, `QUADRO_AQUILA`, `CARTEIRA_BMG`, `CHANGELOG_S1`.

---

## 2️⃣ Inventário · Central de Comando

Decryptado em `Documents/clones-temp/painel-interno/decrypted/index.html`. Tudo dentro de objeto `DADOS = {...}`.

| Aba | data-tab | Sub-estrutura | Função render | HTML específico |
|---|---|---|---|---|
| Visão Geral | `visao` | `DADOS.historico`, `DADOS.equipe` | `renderKpis()` + `renderTabela()` + `renderAlerts()` + `renderDiagnostico()` (2284, 2605, 2679, 2747) | resumo dos KPIs · auto-recalcula |
| Financeira | `financeiro` | `DADOS.historico`, `DADOS.honorarios`, `DADOS.metas`, cenarios | `renderFinanceiroMes(mesKey)` + `renderFinanceiroYTD()` + `renderFinanceiroProjecao()` + `renderFinanceiroAlertasRecs()` (3276, 3501, 3563, 3723) | KPIs · gráficos Chart.js |
| Entradas | `entradas` | `DADOS.entradas` (mensal, porUF, porMotivo, porProduto, uf_mes, alerta_onda_mai) | `renderEntradas()` (3074) | header · 4 KPIs · 3 cards composição · funil mensal · alertas |
| Defesas | `defesas` | `DADOS.equipe`, `DADOS.defesasSemana`, `DADOS.historico[mes].defesas` | `renderDefesasKpis()` + `renderEquipe()` (2309, 2988) | snapshot semanal · ranking colaboradores |
| Encerramentos | `encerramentos` | `DADOS.encerramentos` | `renderEncerramentos()` + `renderEncerramentosKpis()` (2865, 2326) | motivos · evolução |
| Audiências | `audiencias` | `DADOS.audiencias` | `renderAud()` (2633) | virtual/presencial/híbrida |
| Reembolsos | `reembolsos` | `DADOS.reembolsos` (mensal, statusYTD, snapshotPendente, porTipo, porIdade) | `renderReembolsosKpis()` + `renderReembolsos()` (2340, 2917) | header · 4 KPIs · gráfico calculado×creditado · status · tipo · aging (novo) |
| Cenários | `cenarios` | cenarios baseline/otimista/pessimista (3812) | `renderCenarioOutput()` (3861) | simulador interativo |
| Licitações | `licitacoes` | `DADOS.radares` | inline | placeholder · radar futuro |
| Atualizações | `atualizacoes` | `DADOS.changelog` | `renderChangelog()` (3619) | entradas datadas |

---

## 3️⃣ Inventário · Mesa NS

Decryptado em `Documents/Mesa-Executiva-NS/decrypted/index.html`. Estrutura embarca `FATURAMENTO_BMG`, `RGB_DATA_2026`, `CARTEIRA_BMG`, `DECISOES_FINAL`, `RANKING_FORMULA`, `METAS_ANUAIS_BMG`, `MODELOS_INDEX`.

| Seção | onde | Função render | Conteúdo |
|---|---|---|---|
| 🎯 Síntese Executiva (topo) | `#sintese-executiva` | populado por `_atualizar_tudo.py` ou estático | 3 alertas R$ + 3 oportunidades R$ + decisão + justificativa |
| 📊 Cadeia Volume → Receita | `<details>` colapsável | `renderMesaCadeia()` (similar Site 1) | 15 segmentos R×P |
| ⚖️ Balança Financeira what-if | colapsável | simulador interativo JS | sliders enc · % êxito · defesas |
| 🏗 Plano de Produção Modelos | colapsável | estático | 6 modelos priorizados R$ |
| 👥 Briefing 5 setores | colapsável | `renderMesaDiretora()` no Mesa NS | falas dos diretores |
| 💬 Debates estratégicos | colapsável | render inline | 3 temas encadeados |
| 📋 Decisões consolidadas | colapsável | render inline | 5 ações |

**Externo:** `data/estrategia-ativa.json` é gerado pelo `_gera_estrategia.py` e consumido pelo widget azul nos 3 sites via fetch.

---

## 4️⃣ Catálogo de Planilhas

Pra cada planilha conhecida, **TUDO que mexer**.

### A. `Decisões - DD.MM a DD.MM.YYYY.xlsx`
**Fonte:** SharePoint pasta inteligência jurídica BMG · semanal
**Quando chega:** baixar local em Downloads (read_resource trunca!)
**Site 1:**
- Incrementar `DECISOES_FINAL.DECISOES` com novas entradas (Python parseia · 5 lugares: tags reais, UF, causa, resultado, valor)
- Recalcular Matriz UF × Projeto cells (rodar `_probabilidade_uf_projeto.py`)
- Atualizar bloco **Snapshot Semanal** na aba Ranking BMG (Card Decisões · %Fav · UFs · Causas) — HTML estático
- Atualizar contagem global "2.xxx decisões" (replace global)
- `CHANGELOG_S1` entrada nova
**Mesa NS:**
- Atualizar células da Matriz UF × Projeto (espelho)
**Central:** —
**Cross-validation:** % favorável da semana vs YTD · UFs vs base ativa
**Não esquecer (esquecimos antes):** header com banner "EXCEPCIONAL", textos como "+20pp · maior salto" se mudaram

---

### B. `Relatorio defesas Apresentadas - DD.MM a DD.MM.YYYY.xlsx`
**Fonte:** SharePoint pasta Central · semanal
**Central (TODOS os 5 pontos):**
1. `DADOS.equipe` ou `DADOS.equipeSemana` (atualizar contagens por colaborador)
2. `renderDefesasKpis()` (já lê estrutura)
3. HTML estático: **header da aba Defesas** com "Snapshot semanal" — textos DD/MM
4. `card-footer-src` da aba
5. Texto do alerta no `renderEquipe()` se houver
- Atualizar `DADOS.historico[mes].defesas` somando à semana
- Atualizar texto YTD: "X defesas (cobertura até DD/MM)"
- `DADOS.changelog` entrada nova
**Site 1:** —
**Mesa NS:** —
**Cross-validation:** top colaborador vs semana anterior
**Não esquecer:** ranking colaboradores · texto "Top colaboradora" no header

---

### C. `Relatorio Casos novos - DD.MM a DD.MM.YYYY.xlsx`
**Fonte:** SharePoint pasta Central · semanal
**Central:**
- Adicionar ao `DADOS.entradas.mensal` somando ao mês corrente
- Atualizar texto "Junho parcial (126 casos · ritmo voltando)"
- `DADOS.changelog`
**Site 1:** —
**Mesa NS:** —
**Cross-validation:** soma das semanas no mês = total do mês na planilha Ano

---

### D. `Relatorio casos novos Ano 2026.xlsx` (planilha NOVA · 06/2026+)
**Fonte:** Gestor Jurídico BMG · consolidada anual
**Central · aba Entradas (5 pontos):**
1. `DADOS.entradas` REESCRITO inteiro (mensal, porUF, porMotivo, porProduto, uf_mes, ytd_total)
2. `renderEntradas()` (ajustar pra ler YTD)
3. HTML estático: **header source-header** · status pill · 4 KPIs · section-title
4. Card-footers (3) · src-tags · badges
5. Texto alerta hardcoded JS (capacidade vs entrada)
**Site 1 · aba Ranking BMG (bloco Ondas de Entrada):**
- Heatmap UF × Mês · 4 cards · ticket médio causa por UF · 3 verdades
- `faturamento-bmg.json → CASOS_NOVOS_2026_REAL` (matriz · alerta_maio)
- `QUADRO_AQUILA._obs_2` marca fluxo_mensal desatualizado
**Mesa NS:** —
**Cross-validation:** mensal real vs Aquila fluxo_mensal_entrada_saida (até onde válido)

---

### E. `Relatório reembolsos pendentes até DD.MM.YYYY.xlsx`
**Fonte:** SharePoint pasta Central · semanal/quinzenal
**Central · aba Reembolsos (5 pontos):**
1. `DADOS.reembolsos.statusYTD.aguardaReembolso`, `porTipo`, `snapshotPendente`, `porIdade` (NOVO)
2. `renderReembolsos()` + `renderReembolsosKpis()` (já leem)
3. HTML estático: **header source-header** · status pill (warn → ok) · alerta de idade (bloco novo)
4. Card-footers (4) · src-tags (3) · badges "8 tipos"
5. Texto alerta JS dentro renderReembolsos
- `DADOS.changelog`
**Site 1:** —
**Mesa NS:** —
**Cross-validation:** delta itens vs delta valor (sinal duplo) · idade
**Não esquecer:** TODOS os 7 footers/src-tags com fonte velha

---

### F. `Relatorio Gerencial Carteira BMG.xls` (planilha NOVA · 06/2026+ · HTML disfarçado de .xls)
**Fonte:** Gestor Jurídico BMG · snapshot completo
**Processamento:** `pd.read_html()` (não `pd.read_excel`)
**Site 1 · aba Carteira BMG (5 pontos):**
1. `faturamento-bmg.json → CARTEIRA_BMG_GESTOR_JURIDICO` (total, em_curso, encerradas, por_uf, por_produto, por_motivo, aging, delta_vs_aquila)
2. Render do banner novo (estático)
3. HTML estático: source-header novo "Snapshot Gestor Jurídico DD/MM"
4. 4 cards de pulso · tabela Aquila vs Real · aging table · concentração produto×motivo
5. Banner verde de leitura estratégica
**Central:** —
**Mesa NS:** —
**Cross-validation:** EM CURSO vs Aquila base ativa · aging vs tempo médio Aquila

---

### G. `Encerramentos detalhada (motivos).xlsx`
**Fonte:** Email Beatriz mensal · planilha detalhe
**Central · aba Encerramentos (5 pontos):**
1. `DADOS.encerramentos['abril-2026']` etc. (motivos com qtd e valor por mês)
2. `renderEncerramentos()` + `renderEncerramentosKpis()`
3. HTML estático: badges de mês · seletor
4. Card-footers
- `DADOS.historico[mes].encReais=true` · `encFonteOficial`
- `DADOS.changelog`
**Site 1:**
- Atualizar bloco Meta Anual · linha do mês (Ranking BMG)
- `CHANGELOG_S1`
**Mesa NS:**
- `FATURAMENTO_BMG.POR_MES` · encerramentos_qtd + pct_exito + receita_encerramentos
**Cross-validation:** Beatriz vs Aquila (Aquila vence)

---

### H. `PLANILHA AUDIENCIAS.xlsx`
**Fonte:** Central · mensal (eventualmente)
**Status atual:** ⏸️ aguardando próxima versão pra calibrar (decisão 20/05)
**Central · aba Audiências:**
- `DADOS.audiencias` · virtual/presencial/híbrida + receita líquida
- `renderAud()` + KPI no `renderKpis()`
- `DADOS.historico[mes].audVir/audPre/audHib`
**Site 1:** —
**Mesa NS:** `FATURAMENTO_BMG.AUDIENCIAS_MES`

---

### I. Snapshot Quadro Aquila (screenshots)
**Fonte:** dashboard interno do escritório · mensal (dia 14 típico)
**Central:** `faturamento-bmg.json → QUADRO_AQUILA` (6 subseções inteiras) + `POR_MES` (encerramentos, pct_exito, meta_aquila, saldo)
**Site 1 · aba Ranking BMG:**
- Bloco **Pulso Operacional Aquila** (6 gemas) — TODO o painel
- Bloco **Meta Anual** (tabela mensal · Dez/25 a Mai/26)
- Fala CFO/CEO/Estratégico na Mesa Diretora
- `CHANGELOG_S1` · `META_INFO` atualiza
**Mesa NS:** `FATURAMENTO_BMG.POR_MES` · `METAS_ANUAIS_BMG`
**Cross-validation:** Aquila vs Casos novos Ano 2026 (Aquila pode estar parcial — alertar)
**Não esquecer:** se ranking êxito mudou, atualizar Top 5 favoráveis na Matriz UF×Projeto

---

### J. Email Beatriz Duarte (fechamento mensal por produto)
**Fonte:** email · dia 1-3 do mês seguinte
**Central:**
- `DADOS.historico[mes].enc` (oficial!) · `encReais=true` · `encFechado=true` · `encFechadoFonte`
**Site 1 · aba Ranking BMG:**
- Bloco "Resultado Final Maio" (ou mês atual) com 5 produtos · `metaBmg` · `saldoBmg`
- Banner narrativo "Cartão Modalidade falhou em X%"
**Mesa NS:**
- `FATURAMENTO_BMG.POR_MES` (receita_total · receita_encerramentos · obs · fonte_fechamento)

---

### K. BI BMG Performance (screenshot)
**Fonte:** ferramenta BMG · semanal/quinzenal
**Site 1 · aba Régua BMG:**
- `RGB_DATA` array (10-11 clusters Região × Projeto · enc · pctEx · metaEx · tkt · metaTkt)
- Banner leitura estratégica
- `METAS_ANUAIS_BMG` (3 metas anuais: encerramento · exito_pct · ticket_medio)
**Site 1 · aba Ranking BMG:** card 3 metas
**Mesa NS:** `RGB_DATA_2026` (sincronizado com Site 1) · `METAS_ANUAIS_BMG`
**Central:** —

---

### L. `Entradas e Saidas Processos.xlsx` (Gestor Jurídico · estoque)
**Fonte:** Gestor Jurídico BMG · mensal/snapshot
**Status:** processado uma vez em 21/05/2026 · espera próxima versão
**Site 1 · aba Carteira BMG:**
- `CARTEIRA_BMG` total estructure (AGREGADO · POR_PROJETO · POR_UF · POR_PRODUTO · MATRIZ_PROJ_PROD)
- banner data snapshot
- fala CEO/CRO Mesa Diretora
**Mesa NS:** `CARTEIRA_BMG` (sincronizado com Site 1)
**Central:** —

---

## 5️⃣ Pipeline `_processar_planilha.py` (Fase 3)

Script único que detecta tipo da planilha pelo nome e roda o caminho correto.

```bash
python _processar_planilha.py "C:/Users/Rodrigo/Downloads/Decisões - 02.06.2026 a 08.06.2026.xlsx"
# → detecta tipo A · processa · atualiza Site 1 · Mesa NS · valida · encripta · push

python _processar_planilha.py "C:/Users/Rodrigo/Downloads/Relatorio defesas Apresentadas - 02.06.2026 a 08.06.2026.xlsx"
# → detecta tipo B · processa · atualiza Central · ...

python _processar_planilha.py "C:/Users/Rodrigo/Downloads/Relatório reembolsos pendentes até 09.06.2026.xlsx"
# → detecta tipo E · atualiza Central (estrutura + 5 pontos visuais) · push
```

Cada tipo tem **uma função** em Python que encapsula a propagação completa (com base nas tabelas acima).

---

## 📚 Histórico de aprendizados (cabe nos comentários do código)

- 2026-06-10 · **Hotfix Reembolsos:** atualizei DADOS.reembolsos mas esqueci header, status pill e 7 footers. Bug visível pro usuário. → Por isso o ponto **3 (HTML estático)** ficou explícito.
- 2026-06-11 · **Hotfix Entradas:** atualizei tudo mas a aba mostrava 285 entradas (Mai parcial) porque DADOS.entradas só tinha 1 mês. Não atualizei com Casos novos Ano. → Por isso o catálogo ficou explícito por planilha.
- 2026-06-11 · **Mesa NS reestruturada:** 8 painéis duplicados removidos (já viviam no Site 1) · ficaram 6 decisórios + Síntese Executiva no topo. Mesa NS agora é cérebro · não espelho.
