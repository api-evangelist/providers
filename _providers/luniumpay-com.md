---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 60
  human_in_the_loop: 2
  name: Luniumpay Com Agentic Access
  operation_count: 144
  slug: luniumpay-com-agentic-access
  summary_line: 144 operations · 60 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: 'Saldo em USDT do seu projeto: depósito de USDT ou USDC em várias redes e Pix pago com esse saldo (por chave Pix ou Copia e Cola). Chave `lun_test_` usa o simulador: mesmas rotas, formas e estados, nad'
  name: luniumpay-com Carteira USDT API
  slug: luniumpay-com-carteira-usdt-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: PIX entra, cripto sai.
  name: luniumpay-com Cash In API
  slug: luniumpay-com-cash-in-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Cripto entra, PIX sai.
  name: luniumpay-com Cash Out API
  slug: luniumpay-com-cash-out-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: The Cashin API from luniumpay-com — 4 operation(s) for cashin.
  name: luniumpay-com Cashin API
  slug: luniumpay-com-cashin-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: O que dá para liquidar agora. Fonte da verdade — leia daqui em vez de fixar lista.
  name: luniumpay-com Catálogo API
  slug: luniumpay-com-cat-logo-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: A taxa que um parceiro põe por cima da taxa da Lunium, paga pelo usuário final dele, e o saque dessa comissão em cripto.
  name: luniumpay-com Comissão (sub fee) API
  slug: luniumpay-com-comiss-o-sub-fee-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Chave, limites e uso.
  name: luniumpay-com Conta API
  slug: luniumpay-com-conta-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Handoff humano para preço por volume, contrato, parceria ou caso não coberto pela documentação.
  name: luniumpay-com Contato API
  slug: luniumpay-com-contato-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: The Keys API from luniumpay-com — 3 operation(s) for keys.
  name: luniumpay-com Keys API
  slug: luniumpay-com-keys-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Como um agente descobre a Lunium e o que ela faz, sem falar com ninguem.
  name: luniumpay-com Mesh · Discovery API
  slug: luniumpay-com-mesh-discovery-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: 0,10 % sobre volume liquidado de quem voce trouxe. Nada por cadastro.
  name: luniumpay-com Mesh · Economy API
  slug: luniumpay-com-mesh-economy-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Cadastro de agente, credencial e ciclo de vida ate producao.
  name: luniumpay-com Mesh · Identity API
  slug: luniumpay-com-mesh-identity-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Linhagem provada, grafo de indicacoes e volume de rede.
  name: luniumpay-com Mesh · Network API
  slug: luniumpay-com-mesh-network-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Mandate e configuracao de liquidacao do proprio agente.
  name: luniumpay-com Mesh · Policy API
  slug: luniumpay-com-mesh-policy-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: The Payouts API from luniumpay-com — 2 operation(s) for payouts.
  name: luniumpay-com Payouts API
  slug: luniumpay-com-payouts-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: The Pix API from luniumpay-com — 1 operation(s) for pix.
  name: luniumpay-com Pix API
  slug: luniumpay-com-pix-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Fictitious financial journeys and deterministic simulation controls.
  name: luniumpay-com Sandbox API
  slug: luniumpay-com-sandbox-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: Confirmar um PIX sem ser cliente e sem chave.
  name: luniumpay-com Verificação API
  slug: luniumpay-com-verifica-o-api
- baseURL: https://api.luniumpay.com
  baseurl_source: declared
  description: The Webhooks API from luniumpay-com — 3 operation(s) for webhooks.
  name: luniumpay-com Webhooks API
  slug: luniumpay-com-webhooks-api
artifact_total: 37
asyncapis:
- description: ''
  name: Luniumpay Com Webhooks
  slug: luniumpay-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/luniumpay-com/agentic-access/luniumpay-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/luniumpay-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/luniumpay-com/rules/luniumpay-com-rules.yml
  title: ''
  type: Spectral
  url: rules/luniumpay-com-rules.yml
- group: design
  href: https://artifacts.apis.io/luniumpay-com/json-ld/luniumpay-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/luniumpay-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/luniumpay-com/vocabulary/luniumpay-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/luniumpay-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/luniumpay-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/luniumpay-com/asyncapi/luniumpay-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/luniumpay-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/luniumpay-com/data-model/luniumpay-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/luniumpay-com-data-model.yml
- group: start
  href: https://artifacts.apis.io/luniumpay-com/sandbox/luniumpay-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/luniumpay-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/luniumpay-com/errors/luniumpay-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/luniumpay-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/luniumpay-com/conformance/luniumpay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/luniumpay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/luniumpay-com/llms/luniumpay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/luniumpay-com-llms.txt
- group: other
  href: https://artifacts.apis.io/luniumpay-com/a2a/luniumpay-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/luniumpay-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/luniumpay-com/mcp/luniumpay-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/luniumpay-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/luniumpay-com/well-known/luniumpay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/luniumpay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/luniumpay-com/hosts/luniumpay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/luniumpay-com-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.luniumpay.com/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LuniumPay
- group: docs
  title: ''
  type: APIReference
  url: https://docs.luniumpay.com/
- group: auth
  href: https://artifacts.apis.io/luniumpay-com/authentication/luniumpay-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/luniumpay-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/luniumpay-com/security/luniumpay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/luniumpay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://luniumpay.com/
created: '2026-10-30'
description: LuniumPay provides a comprehensive API for Pix payments, stablecoin transfers, and on‑ramp/off‑ramp services. It targets fintechs, e‑commerce platforms, and international traders, offering solutions for payments, settlements, and compliance. The platform includes detailed documentation, sandbox environments, and AI‑assisted integration guides, supporting multiple languages and currencies.
image: https://luniumpay.com/assets/logo.png
json_schemas:
- name: CashOut
  property_count: 45
  slug: luniumpay-com-cash-out
- name: CatalogoCompra
  property_count: 6
  slug: luniumpay-com-catalogo-compra
- name: ChaveMe
  property_count: 8
  slug: luniumpay-com-chave-me
- name: Cobranca
  property_count: 32
  slug: luniumpay-com-cobranca
- name: Payout
  property_count: 24
  slug: luniumpay-com-payout
- name: StatusCobranca
  property_count: 41
  slug: luniumpay-com-status-cobranca
jsonld:
- class_count: 38
  name: Luniumpay Com Context
  property_count: 293
  slug: luniumpay-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.luniumpay.com.
  name: luniumpay-com MCP Server
  slug: luniumpay-com-mcp-yml
modified: '2026-10-30'
name: luniumpay-com
nav: Providers
network: true
overview: 'luniumpay-com publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Carteira USDT API, Cash In API, Cash Out API, and 16 more. Tagged areas include Company, Payments, Fintech, API, and Pix.


  The luniumpay-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  luniumpay-com''s developer surface includes sandbox, API reference, authentication, and 18 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: luniumpay-com API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 1
  slug: luniumpay-com-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 72.5
    developer_ergonomics: 28.0
    discoverability: 65.0
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Luniumpay Com Authentication
  slug: luniumpay-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Luniumpay Com Domain Security
  slug: luniumpay-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: luniumpay-com-cash-out-flow
  slug: luniumpay-com-cash-out-flow
- name: luniumpay-com-cashin-create-charge
  slug: luniumpay-com-cashin-create-charge
- name: luniumpay-com-check-balance
  slug: luniumpay-com-check-balance
- name: luniumpay-com-mesh-network-workflow
  slug: luniumpay-com-mesh-network-workflow
- name: luniumpay-com-register-validate-activate-agent
  slug: luniumpay-com-register-validate-activate-agent
slug: luniumpay-com
tags:
- Company
- Payments
- Fintech
- API
- Pix
- Stablecoin
website: https://luniumpay.com/
---
