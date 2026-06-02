"""
Varredura semanal de notícias jurídicas para a carteira BMG.

Chama Claude API com tool de web_search, busca notícias dos últimos 7 dias
nas principais fontes jurídicas (STJ, Conjur, JOTA, Agência Brasil, etc.),
filtra por relevância pra carteira BMG (consignado, RMC/RCC, fraude, biometria,
dano moral), e produz:

1. Array de notícias estruturadas pra inserir no NEWS do Site 1
2. Lista de modelos do SharePoint sugeridos pra revisão (baseado nas teses novas)
3. Briefing markdown executivo com tudo

Configurado para uso no GitHub Actions. Variável de ambiente esperada:
    ANTHROPIC_API_KEY · key da Anthropic Console (https://console.anthropic.com)

Saída:
    1. atualiza decrypted/index.html (array NEWS + rótulo varredura + changelog)
    2. encripta index.html via staticrypt (chamado pelo workflow após este script)
    3. salva briefings-semanais/YYYY-MM-DD.md
    4. salva briefing-latest.md (pra issue do GitHub Actions ler)

Exit code: 0 = sucesso · 1 = nada relevante (sem mudanças) · 2 = erro
"""
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

from anthropic import Anthropic

MODEL = "claude-sonnet-4-5-20250929"  # melhor custo-benefício pra esta tarefa
DECRYPTED_PATH = Path("decrypted/index.html")
BRIEFINGS_DIR = Path("briefings-semanais")
BRIEFING_LATEST = Path("briefing-latest.md")


# ─── Carregamento e parsing do HTML atual ──────────────────────────────
def load_html() -> str:
    if not DECRYPTED_PATH.exists():
        raise FileNotFoundError(f"Arquivo {DECRYPTED_PATH} não encontrado. O workflow deve descriptografar primeiro.")
    return DECRYPTED_PATH.read_text(encoding="utf-8")


def extract_news_array(html: str) -> tuple[str, int, int]:
    """Localiza o array `const NEWS = [...]` e retorna (conteúdo, start_idx, end_idx)."""
    start_match = re.search(r"const NEWS = \[", html)
    if not start_match:
        raise ValueError("Marker 'const NEWS = [' não encontrado")
    start = start_match.start()
    # Conta colchetes pra achar o fim
    depth = 0
    i = start_match.end() - 1  # posição do `[`
    while i < len(html):
        c = html[i]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                # Procura o `;` após
                j = i + 1
                while j < len(html) and html[j] != ";":
                    j += 1
                return html[start : j + 1], start, j + 1
        i += 1
    raise ValueError("Fim do array NEWS não encontrado")


def extract_modelos_index(html: str) -> list[dict]:
    """Extrai a constante MODELOS_INDEX como lista de dicionários."""
    match = re.search(r"const MODELOS_INDEX = (\[.*?\]);", html, re.DOTALL)
    if not match:
        return []
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return []


def extract_existing_news_titles(news_block: str) -> list[str]:
    """Pega títulos das notícias já presentes pra evitar duplicação."""
    return re.findall(r"titulo:\s*'([^']+)'", news_block)


# ─── Prompt e chamada à API ────────────────────────────────────────────
def build_prompt(modelos: list[dict], titulos_existentes: list[str]) -> str:
    hoje = datetime.now().strftime("%Y-%m-%d")
    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    modelos_resumo = "\n".join(
        f"- {m['nome']} ({m['categoria']}/{m.get('subcategoria', '')}) · equipe {m['equipe']} · lastMod {m.get('lastMod', '?')}"
        for m in modelos
    )

    titulos_str = "\n".join(f"- {t}" for t in titulos_existentes[:15])

    return f"""Você é um analista jurídico especializado em direito bancário, contencioso de massa
e regulação do crédito consignado. Sua tarefa é a varredura semanal de notícias jurídicas
relevantes para a operação do escritório Nepomuceno Soares Advogados Associados,
que defende o banco BMG em ações de cartão consignado (RMC/RCC), modalidade,
fraude, alegação de não reconhecimento e similares.

DATA DE HOJE: {hoje}
PERÍODO A VARRER: últimos 7 dias ({seven_days_ago} a {hoje})

## OBJETIVO

Buscar nas fontes abaixo e filtrar notícias dos últimos 7 dias que afetem:
- STJ Temas 1.328 (dano moral in re ipsa RMC) e 1.414 (validade RMC/RCC)
- Regulação do consignado INSS (Lei 15.327/2026, MP 1.355/2026, biometria)
- Decisões de tribunais regionais (TJSP, TJMG, TJRS, TJSC, TJPR, TJRJ, TJES)
- Reformas legislativas/regulatórias do consignado, cartão consignado, RMC, RCC
- Súmulas, IRDR, IAC novos
- Provimentos/Resoluções CNJ, AGU, TCU, Min. Trabalho, Min. Previdência sobre consignado

## FONTES A CONSULTAR (use web_search)

1. STJ portal de notícias (stj.jus.br)
2. Conjur (conjur.com.br)
3. JOTA (jota.info) e Migalhas (migalhas.com.br)
4. Agência Brasil (agenciabrasil.ebc.com.br)
5. CNJ (cnj.jus.br)
6. ABRADEB (abradeb.com.br)

Busque com queries variadas: "STJ Tema 1.414", "STJ Tema 1.328", "consignado INSS",
"RMC RCC decisão", "cartão consignado fraude", "dano moral consignado", "biometria
consignado", "litigância abusiva consignado", e variações.

## NOTÍCIAS JÁ EXISTENTES NO SITE (NÃO duplicar)

{titulos_str}

## MODELOS DO SHAREPOINT DO ESCRITÓRIO (cruze com as notícias)

{modelos_resumo}

## FORMATO DE SAÍDA OBRIGATÓRIO (JSON estrito)

Responda APENAS com um JSON válido, sem texto antes nem depois, no schema:

{{
  "data_varredura": "{hoje}",
  "noticias_novas": [
    {{
      "id": "n12",
      "impacto": "critico" | "relevante" | "informativo",
      "causas": ["modalidade" | "fraude" | "cadastro"],
      "titulo": "string curta (máx 120 chars)",
      "fonte": "STJ / Conjur / Agência Brasil / etc.",
      "data": "DD mmm YYYY",
      "resumo": "string com 2-4 frases descrevendo o que rolou. Pode usar <b> pra destacar termos chave.",
      "impactoModelos": "string com AÇÃO IMEDIATA, AÇÃO CONTINUADA ou MONITORAR + o que fazer em concreto",
      "url": "URL completa da fonte"
    }}
  ],
  "modelos_sugeridos_atualizar": [
    {{
      "modelo_nome": "nome exato do modelo do MODELOS_INDEX",
      "razao": "frase curta explicando por quê",
      "argumento_a_adicionar": "string com o argumento/tese específica que deveria entrar no modelo"
    }}
  ],
  "briefing_executivo": "string em markdown com 4-8 parágrafos cobrindo: (1) o que aconteceu de mais importante na semana · (2) ações urgentes pra equipe · (3) modelos a revisar · (4) status dos Temas STJ pendentes · (5) próxima coisa a monitorar. Foco operacional, sem números financeiros do escritório."
}}

REGRAS CRÍTICAS:
- ids das notícias devem começar do número seguinte ao último nID existente
- impacto = critico só pra leis novas, decisões vinculantes, mudanças regulatórias amplas
- impacto = relevante pra doutrina forte, sobrestamentos, decisões setoriais
- impacto = informativo pra coisas que valem acompanhar mas sem urgência
- Se NADA relevante surgiu nos últimos 7 dias: retornar noticias_novas: [] e briefing_executivo explicando que a semana foi de "manutenção do cenário" sem novidades pra registrar
- Cada modelo_sugeridos_atualizar deve corresponder a um modelo_nome EXISTENTE na lista MODELOS_INDEX acima
- NUNCA inventar URLs. Se não encontrou fonte concreta, omita a notícia.
"""


def call_claude(prompt: str) -> dict:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY não definida no ambiente")

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model=MODEL,
        max_tokens=8192,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 8}],
        messages=[{"role": "user", "content": prompt}],
    )

    # Extrai o último bloco de texto da resposta (após uso de tools)
    text_chunks = [b.text for b in response.content if hasattr(b, "text") and b.text]
    if not text_chunks:
        raise RuntimeError("Resposta da API não contém texto")
    final_text = text_chunks[-1].strip()

    # Remove cercas markdown se houver
    if final_text.startswith("```json"):
        final_text = final_text[7:]
    elif final_text.startswith("```"):
        final_text = final_text[3:]
    if final_text.endswith("```"):
        final_text = final_text[:-3]
    final_text = final_text.strip()

    return json.loads(final_text)


# ─── Atualização do HTML ────────────────────────────────────────────────
def render_news_object(n: dict) -> str:
    """Renderiza um objeto de notícia no formato JS embedded."""
    def esc(s: str) -> str:
        return str(s).replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ").strip()

    causas_str = ",".join(f"'{c}'" for c in n.get("causas", []))
    return (
        "  {\n"
        f"    id:'{esc(n['id'])}', impacto:'{esc(n['impacto'])}', causas:[{causas_str}],\n"
        f"    titulo:'{esc(n['titulo'])}',\n"
        f"    fonte:'{esc(n['fonte'])}', data:'{esc(n['data'])}',\n"
        f"    resumo:'{esc(n['resumo'])}',\n"
        f"    impactoModelos:'{esc(n['impactoModelos'])}',\n"
        f"    url:'{esc(n['url'])}'\n"
        "  }"
    )


def update_html(html: str, noticias_novas: list[dict]) -> str:
    if not noticias_novas:
        return html

    news_block, start, end = extract_news_array(html)
    # Insere as novas notícias logo após o `[` inicial
    open_bracket = news_block.find("[") + 1
    novas_str = "\n" + ",\n".join(render_news_object(n) for n in noticias_novas) + ","
    new_news_block = news_block[:open_bracket] + novas_str + news_block[open_bracket:]
    new_html = html[:start] + new_news_block + html[end:]

    # Atualiza rótulo "Última varredura"
    hoje_str = datetime.now().strftime("%d/%m/%Y")
    n_str = f"{len(noticias_novas)} notícia{'s' if len(noticias_novas) > 1 else ''} nova{'s' if len(noticias_novas) > 1 else ''}"
    new_html = re.sub(
        r"(Última varredura:\s*<b>)[^<]+(</b>[^<]*)",
        rf"\g<1>{hoje_str}\g<2>",
        new_html,
        count=1,
    )

    # Adiciona entrada no changelog (no topo do array CHANGELOG_S1)
    changelog_entry = (
        "  {\n"
        f"    data:'{datetime.now().strftime('%Y-%m-%d')}', hora:'09:00', versao:'auto', commit:'(pendente)',\n"
        f"    tipo:'data-refresh',\n"
        f"    titulo:'Varredura semanal automática · {n_str}',\n"
        f"    resumo:'Workflow GitHub Actions chamou Claude API e adicionou {n_str} ao array NEWS. Ver briefing em briefings-semanais/{datetime.now().strftime('%Y-%m-%d')}.md.',\n"
        "    arquivos:[],\n"
        "    abas:['Inteligência de Mercado (auto)']\n"
        "  },\n"
    )
    new_html = re.sub(
        r"(const CHANGELOG_S1 = \[\n)",
        rf"\g<1>{changelog_entry}",
        new_html,
        count=1,
    )

    return new_html


# ─── Briefing markdown ──────────────────────────────────────────────────
def build_briefing_markdown(result: dict) -> str:
    hoje = result.get("data_varredura", datetime.now().strftime("%Y-%m-%d"))
    noticias = result.get("noticias_novas", [])
    modelos = result.get("modelos_sugeridos_atualizar", [])
    executivo = result.get("briefing_executivo", "(briefing executivo não foi gerado)")

    lines = [
        f"# 📰 Briefing semanal · {hoje}",
        "",
        "_Gerado automaticamente pela varredura semanal de notícias jurídicas (GitHub Actions + Claude API)._",
        "",
        "---",
        "",
        "## 🎯 Resumo executivo",
        "",
        executivo,
        "",
        "---",
        "",
        f"## 📋 Notícias adicionadas ao Site 1 ({len(noticias)})",
        "",
    ]

    if not noticias:
        lines.append("_Nenhuma notícia nova relevante detectada nos últimos 7 dias. Cenário de manutenção._")
    else:
        for n in noticias:
            badge = {"critico": "🔴 CRÍTICO", "relevante": "🟡 RELEVANTE", "informativo": "ℹ️ INFORMATIVO"}.get(
                n.get("impacto", "informativo"), "ℹ️"
            )
            lines.extend([
                f"### {badge} · {n.get('titulo', '?')}",
                "",
                f"**Fonte:** {n.get('fonte', '?')} · **Data:** {n.get('data', '?')}",
                "",
                f"**Resumo:** {re.sub('<[^<]+?>', '', n.get('resumo', ''))}",
                "",
                f"**Impacto nos modelos:** {re.sub('<[^<]+?>', '', n.get('impactoModelos', ''))}",
                "",
                f"**URL:** {n.get('url', '—')}",
                "",
                "---",
                "",
            ])

    lines.extend([
        f"## 🔧 Modelos sugeridos pra revisão ({len(modelos)})",
        "",
    ])
    if not modelos:
        lines.append("_Nenhum modelo precisa de revisão imediata baseado nas notícias dessa semana._")
    else:
        for m in modelos:
            lines.extend([
                f"### {m.get('modelo_nome', '?')}",
                f"- **Razão:** {m.get('razao', '?')}",
                f"- **Argumento a adicionar:** {m.get('argumento_a_adicionar', '?')}",
                "",
            ])

    lines.extend([
        "---",
        "",
        "## ✅ Próximos passos",
        "",
        "1. Equipe Recursal / Defesa: revisar os modelos listados acima",
        "2. Coordenação: avaliar se alguma notícia exige comunicado interno",
        "3. Próxima varredura: segunda-feira da próxima semana, 9h",
        "",
        f"_Workflow: `.github/workflows/varredura-noticias.yml` · briefing salvo em `briefings-semanais/{hoje}.md`_",
    ])

    return "\n".join(lines)


# ─── Main ───────────────────────────────────────────────────────────────
def main() -> int:
    print(f"[{datetime.now().isoformat()}] Iniciando varredura semanal de notícias jurídicas")

    try:
        html = load_html()
        news_block, _, _ = extract_news_array(html)
        modelos = extract_modelos_index(html)
        titulos_existentes = extract_existing_news_titles(news_block)
        print(f"  · {len(modelos)} modelos no índice · {len(titulos_existentes)} notícias existentes")

        prompt = build_prompt(modelos, titulos_existentes)
        print("  · Chamando Claude API com web_search habilitado…")
        result = call_claude(prompt)

        noticias_novas = result.get("noticias_novas", [])
        modelos_sug = result.get("modelos_sugeridos_atualizar", [])
        print(f"  · Claude retornou {len(noticias_novas)} notícia(s) nova(s), {len(modelos_sug)} modelo(s) sugerido(s)")

        # Gera briefing sempre (mesmo se 0 notícias)
        BRIEFINGS_DIR.mkdir(parents=True, exist_ok=True)
        briefing = build_briefing_markdown(result)
        hoje = datetime.now().strftime("%Y-%m-%d")
        (BRIEFINGS_DIR / f"{hoje}.md").write_text(briefing, encoding="utf-8")
        BRIEFING_LATEST.write_text(briefing, encoding="utf-8")
        print(f"  · Briefing salvo em {BRIEFINGS_DIR / f'{hoje}.md'}")

        if not noticias_novas:
            print("[OK] Nada novo relevante detectado · cenário de manutenção")
            return 1  # signal pro workflow não commitar mudanças no HTML

        # Atualiza HTML
        new_html = update_html(html, noticias_novas)
        DECRYPTED_PATH.write_text(new_html, encoding="utf-8")
        print(f"[OK] HTML atualizado com {len(noticias_novas)} notícia(s)")
        return 0

    except Exception as e:
        print(f"[ERRO] {type(e).__name__}: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
