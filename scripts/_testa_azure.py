# -*- coding: utf-8 -*-
"""
Teste de conexão ao Azure/Microsoft Graph (app "BMG Sites Sync").
Lê AZURE_TENANT_ID/CLIENT_ID/CLIENT_SECRET do env OU de scripts/.env (gitignored).
NUNCA imprime o secret. Diz só se conectou (token obtido) ou o erro exato.

Uso:  python scripts/_testa_azure.py
"""
import os, sys
from pathlib import Path

# carrega scripts/.env se existir (parse simples · sem dependência extra)
envf = Path(__file__).resolve().parent / '.env'
if envf.exists():
    for line in envf.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line and not line.startswith('#') and '=' in line:
            k, v = line.split('=', 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

t = os.environ.get('AZURE_TENANT_ID')
c = os.environ.get('AZURE_CLIENT_ID')
s = os.environ.get('AZURE_CLIENT_SECRET')

falta = [k for k, v in [('AZURE_TENANT_ID', t), ('AZURE_CLIENT_ID', c), ('AZURE_CLIENT_SECRET', s)] if not v]
if falta:
    print('❌ Faltam credenciais:', ', '.join(falta))
    print('   → copie scripts/.env.exemplo para scripts/.env e preencha (ou defina as env vars).')
    sys.exit(1)

# sanidade dos IDs (sem revelar): tenant/client devem parecer GUIDs
def guid_ok(x): return len(x) >= 32 and x.count('-') == 4
print('Tenant ID :', 'formato de GUID ok' if guid_ok(t) else '⚠ não parece um GUID')
print('Client ID :', 'formato de GUID ok' if guid_ok(c) else '⚠ não parece um GUID')
print('Secret    :', f'presente ({len(s)} chars)')
print('Conectando ao Microsoft Graph (client credentials)...')

try:
    import msal
except ImportError:
    print('❌ msal não instalado · rode: python -m pip install msal requests'); sys.exit(2)

app = msal.ConfidentialClientApplication(
    c, authority=f'https://login.microsoftonline.com/{t}', client_credential=s)
r = app.acquire_token_for_client(scopes=['https://graph.microsoft.com/.default'])

if 'access_token' in r:
    print('\n✅ CONECTOU · token obtido do Graph · expira em', r.get('expires_in'), 's.')
    print('   O app "BMG Sites Sync" está autenticando. Próximo passo: rodar o sharepoint_audit.py')
    print('   e atualizar o GitHub secret AZURE_CLIENT_SECRET pra o vigia voltar a rodar.')
    sys.exit(0)
else:
    err = r.get('error'); desc = str(r.get('error_description', ''))[:300]
    print('\n❌ NÃO conectou ·', err)
    print('   ', desc)
    # dicas por erro comum
    if err == 'invalid_client' or 'AADSTS7000215' in desc or 'AADSTS7000222' in desc:
        print('   → secret errado ou EXPIRADO. Gere um novo em Certificates & secrets.')
    elif 'AADSTS700016' in desc or err == 'unauthorized_client':
        print('   → client_id/tenant errado, ou app não existe nesse tenant.')
    elif 'AADSTS90002' in desc:
        print('   → tenant_id errado.')
    sys.exit(3)
