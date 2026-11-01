---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Banco Inter Agentic Access
  operation_count: 112
  slug: banco-inter-agentic-access
  summary_line: 112 operations · 62 acting
api_count: 9
apis:
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Boletos API from Banco Inter — 5 operation(s) for boletos.
  name: Banco Inter Boletos API
  slug: banco-inter-boletos-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Cobrança API from Banco Inter — 7 operation(s) for cobrança.
  name: Banco Inter Cobrança API
  slug: banco-inter-cobran-a-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Cobrança com Vencimento API from Banco Inter — 4 operation(s) for cobrança com vencimento.
  name: Banco Inter Cobrança com Vencimento API
  slug: banco-inter-cobran-a-com-vencimento-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Cobrança com Vencimento em Lote API from Banco Inter — 4 operation(s) for cobrança com vencimento em lote.
  name: Banco Inter Cobrança com Vencimento em Lote API
  slug: banco-inter-cobran-a-com-vencimento-em-lote-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Cobrança Imediata API from Banco Inter — 4 operation(s) for cobrança imediata.
  name: Banco Inter Cobrança Imediata API
  slug: banco-inter-cobran-a-imediata-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: Esta seção apresenta os endpoints relacionados ao gerenciamento de cobranças associadas a uma recorrência. As cobranças só poderão ser geradas utilizando este endpoint após a recorrência ser autorizad
  name: Banco Inter Cobrança Recorrente API
  slug: banco-inter-cobran-a-recorrente-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Extrato API from Banco Inter — 3 operation(s) for extrato.
  name: Banco Inter Extrato API
  slug: banco-inter-extrato-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Location API from Banco Inter — 3 operation(s) for location.
  name: Banco Inter Location API
  slug: banco-inter-location-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: Esta seção apresenta os endpoints relacionados ao gerenciamento de payloads associadas a uma recorrência. ---
  name: Banco Inter Location da Recorrência API
  slug: banco-inter-location-da-recorr-ncia-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Pagamento API from Banco Inter — 5 operation(s) for pagamento.
  name: Banco Inter Pagamento API
  slug: banco-inter-pagamento-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Pix API from Banco Inter — 3 operation(s) for pix.
  name: Banco Inter Pix API
  slug: banco-inter-pix-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Pix Pagamento API from Banco Inter — 2 operation(s) for pix pagamento.
  name: Banco Inter Pix Pagamento API
  slug: banco-inter-pix-pagamento-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Proposta API from Banco Inter — 1 operation(s) for proposta.
  name: Banco Inter Proposta API
  slug: banco-inter-proposta-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Publicação API from Banco Inter — 2 operation(s) for publicação.
  name: Banco Inter Publicação API
  slug: banco-inter-publica-o-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: Essa seção apresenta os endpoints relacionados ao gerenciamento de recorrências do Pix Automático. Para que as cobranças sejam geradas automaticamente para os clientes pagadores, devemos criar uma rec
  name: Banco Inter Recorrência API
  slug: banco-inter-recorr-ncia-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Saldo API from Banco Inter — 1 operation(s) for saldo.
  name: Banco Inter Saldo API
  slug: banco-inter-saldo-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: Esta seção apresenta os endpoints relacionados ao gerenciamento de solicitações de confirmação de recorrência, que equivalem às autorizações necessárias. Para que as recorrências tenham validade e pos
  name: Banco Inter Solicitar Recorrência API
  slug: banco-inter-solicitar-recorr-ncia-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Token API from Banco Inter — 1 operation(s) for token.
  name: Banco Inter Token API
  slug: banco-inter-token-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Upload de mídia API from Banco Inter — 1 operation(s) for upload de mídia.
  name: Banco Inter Upload de mídia API
  slug: banco-inter-upload-de-m-dia-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Webhook API from Banco Inter — 8 operation(s) for webhook.
  name: Banco Inter Webhook API
  slug: banco-inter-webhook-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: Esta seção apresenta os endpoints relacionados ao gerenciamento do serviço de notificações de cobranças recorrentes. ---
  name: Banco Inter Webhook de Cobranças Recorrentes API
  slug: banco-inter-webhook-de-cobran-as-recorrentes-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: The Webhook de Pix Cobrança API from Banco Inter — 3 operation(s) for webhook de pix cobrança.
  name: Banco Inter Webhook de Pix Cobrança API
  slug: banco-inter-webhook-de-pix-cobran-a-api
- baseURL: https://cdpj.partners.bancointer.com.br/oauth/v2
  baseurl_source: declared
  description: Esta seção apresenta os endpoints relacionados ao gerenciamento do serviço de notificações acerca de recorrências. ---
  name: Banco Inter Webhook de Recorrências API
  slug: banco-inter-webhook-de-recorr-ncias-api
artifact_total: 81
asyncapis:
- description: ''
  name: Banco Inter Webhooks
  slug: banco-inter-webhooks
common:
- group: other
  href: https://artifacts.apis.io/banco-inter/capabilities/banco-inter-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/banco-inter-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/banco-inter/agentic-access/banco-inter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/banco-inter-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/banco-inter/rate-limits/banco-inter-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/banco-inter-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/rules/banco-inter-rules.yml
  title: ''
  type: Spectral
  url: rules/banco-inter-rules.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/json-ld/banco-inter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/banco-inter-context.jsonld
- group: design
  href: https://artifacts.apis.io/banco-inter/vocabulary/banco-inter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/banco-inter-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/banco-inter/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/asyncapi/banco-inter-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/banco-inter-webhooks.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/data-model/banco-inter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/banco-inter-data-model.yml
- group: operate
  href: https://artifacts.apis.io/banco-inter/changelog/banco-inter-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/banco-inter-changelog.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/conventions/banco-inter-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/banco-inter-conventions.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/conventions/banco-inter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/banco-inter-conventions.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/lifecycle/banco-inter-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/banco-inter-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/errors/banco-inter-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/banco-inter-problem-types.yml
- group: design
  href: https://artifacts.apis.io/banco-inter/conformance/banco-inter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/banco-inter-conformance.yml
- group: other
  href: https://artifacts.apis.io/banco-inter/overlays/banco-inter-banking-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/banco-inter-banking-overlay.yaml
- group: build
  href: https://artifacts.apis.io/banco-inter/mcp/banco-inter-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/banco-inter-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/banco-inter/well-known/banco-inter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banco-inter-well-known.yml
- group: other
  href: https://artifacts.apis.io/banco-inter/hosts/banco-inter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banco-inter-hosts.yml
- group: other
  href: https://artifacts.apis.io/banco-inter/vendors/banco-inter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banco-inter-vendors.yml
- group: build
  href: https://artifacts.apis.io/banco-inter/packages/banco-inter-packages.yml
  title: ''
  type: Packages
  url: packages/banco-inter-packages.yml
- group: auth
  href: https://artifacts.apis.io/banco-inter/authentication/banco-inter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/banco-inter-authentication.yml
- group: auth
  href: https://artifacts.apis.io/banco-inter/scopes/banco-inter-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/banco-inter-scopes.yml
- group: auth
  href: https://artifacts.apis.io/banco-inter/security/banco-inter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banco-inter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bancointer.com.br
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.inter.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.inter.co/docs/introducao/sobre-este-portal
- group: docs
  title: ''
  type: APIReference
  url: https://developers.inter.co/references/token
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.inter.co/changelog
- group: start
  title: ''
  type: Sandbox
  url: https://developers.inter.co/sandbox
- group: build
  title: ''
  type: SDKs
  url: https://developers.inter.co/docs/sdks/sdk-intro
- group: agent
  title: ''
  type: MCPServer
  url: https://developers.inter.co/docs/mcp/visao-geral
- group: operate
  title: ''
  type: FAQ
  url: https://developers.inter.co/duvidas-frequentes
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.inter.co/erros-status-code
- group: operate
  title: ''
  type: Support
  url: https://developers.inter.co/contacts
- group: operate
  title: ''
  type: Community
  url: https://comunidade.inter.co/developers
- group: operate
  title: ''
  type: HelpCenter
  url: https://ajuda.inter.co/
- group: company
  title: ''
  type: Blog
  url: https://blog-us.inter.co
- group: company
  title: ''
  type: Newsroom
  url: https://inter.co/news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.inter.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inter-co
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inter.co/politica-de-privacidade/
- group: auth
  title: ''
  type: Security
  url: https://inter.co/en/security/
created: '2026-10-18'
description: 'Banco Inter (Inter&Co, Nasdaq: INTR) is a Brazilian digital bank and financial super app offering free digital checking accounts, payments, Pix, credit, investments, insurance and an international Global Account. Its Inter Empresas developer portal (developers.inter.co) documents business banking APIs secured with mTLS certificates and OAuth 2.0: statements (Extrato), balances (Saldos), payments, Pix Cobrança, Pix Pagamento, Pix Automático and boleto collection (Cobrança), plus webhooks, a sandbox environment, SDKs (Java, C#, Python, PHP), CNAB file tooling and an MCP server.'
image: https://developers.inter.co/img/inter-empresas-logo.svg
json_schemas:
- name: baixaBoletoRequest
  property_count: 1
  slug: banco-inter-baixa-boleto-request
- name: boletoResponse
  property_count: 25
  slug: banco-inter-boleto-response
- name: Boletos Consultados
  property_count: 7
  slug: banco-inter-boletos-page-response
- name: CallbackAttemptPage
  property_count: 5
  slug: banco-inter-callback-attempt-page
- name: Cobrança imediata gerada
  property_count: 0
  slug: banco-inter-cob-gerada
- name: Cobrança Recorrente Completa
  property_count: 0
  slug: banco-inter-cob-rcompleta
- name: Cobrança Recorrente Gerada
  property_count: 0
  slug: banco-inter-cob-rgerada
- name: Cobrança com vencimento gerada
  property_count: 0
  slug: banco-inter-cob-vgerada
- name: CobrancaDetalhadaResponseBody
  property_count: 4
  slug: banco-inter-cobranca-detalhada-response-body
- name: Cobranças Consultadas
  property_count: 7
  slug: banco-inter-cobrancas-response
- name: Devolução
  property_count: 6
  slug: banco-inter-devolucao
- name: GenerateUploadUrlRequest
  property_count: 1
  slug: banco-inter-generate-upload-url-request
- name: GenerateUploadUrlResponse
  property_count: 2
  slug: banco-inter-generate-upload-url-response
- name: incluiBoletoRequest
  property_count: 12
  slug: banco-inter-inclui-boleto-request
- name: incluiBoletoResponse
  property_count: 4
  slug: banco-inter-inclui-boleto-response
- name: InformacoesPagamento
  property_count: 17
  slug: banco-inter-informacoes-pagamento-darf
- name: InformacoesPagamento
  property_count: 16
  slug: banco-inter-informacoes-pagamento
- name: itemSumarioCobrancas
  property_count: 3
  slug: banco-inter-item-sumario-cobrancas
- name: ListaTransacoesCompletaScroll
  property_count: 4
  slug: banco-inter-lista-transacoes-completa-scroll
- name: Lote de solicitações de alteração ou criação de cobranças com vencimento
  property_count: 4
  slug: banco-inter-lote-cob-vconsultado
- name: ObterLoteResponse
  property_count: 3
  slug: banco-inter-obter-lote-response
- name: Operacao
  property_count: 3
  slug: banco-inter-operacao
- name: PagamentoPixResponse
  property_count: 4
  slug: banco-inter-pagamento-pix-response
- name: Location do Payload Completa
  property_count: 3
  slug: banco-inter-payload-location-rec-gerada
- name: Pix
  property_count: 8
  slug: banco-inter-pix
- name: Proposta
  property_count: 4
  slug: banco-inter-proposta
- name: PublicationPageResponse
  property_count: 3
  slug: banco-inter-publication-page-response
- name: PublicationRequestBody
  property_count: 6
  slug: banco-inter-publication-request-body
- name: PublicationResponse
  property_count: 13
  slug: banco-inter-publication-response
- name: Recorrência Completa
  property_count: 0
  slug: banco-inter-rec-completa
- name: Recorrência Gerada
  property_count: 0
  slug: banco-inter-rec-gerada
- name: Saldo
  property_count: 6
  slug: banco-inter-saldo
- name: Solicitação de Recorrência Completa
  property_count: 0
  slug: banco-inter-solic-rec-completa
- name: TokenRequest
  property_count: 4
  slug: banco-inter-token-request
- name: UpdateCobrancaResponseBody
  property_count: 3
  slug: banco-inter-update-cobranca-response-body
- name: UpdatePublicationRequestBody
  property_count: 3
  slug: banco-inter-update-publication-request-body
- name: Webhook
  property_count: 3
  slug: banco-inter-webhook-completo
jsonld:
- class_count: 120
  name: Banco Inter Context
  property_count: 239
  slug: banco-inter-context
layout: provider
mcp_servers:
- description: ''
  name: Banco Inter MCP Server
  slug: visao-geral
modified: '2026-10-18'
name: Banco Inter
nav: Providers
network: true
overview: 'Banco Inter publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Boletos API, Cobrança API, Cobrança com Vencimento API, and 20 more. Tagged areas include Company, Banking, Fintech, Payments, and Pix.


  The Banco Inter catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Banco Inter''s developer surface includes changelog, authentication, documentation, API reference, sandbox, FAQ, support, and 36 more developer resources.'
plans:
- name: Banco Inter Plans Pricing
  plan_count: 0
  slug: banco-inter-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Banco Inter Rate Limits
  slug: banco-inter-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Banco Inter API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: banco-inter-rules
scopes:
- name: Banco Inter Scopes
  scope_count: 2
  slug: banco-inter-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.8
    catalog_earned_first_party: 0.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 67.8
    developer_ergonomics: 61.3
    discoverability: 71.7
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Banco Inter Authentication
  slug: banco-inter-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Banco Inter Domain Security
  slug: banco-inter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 11
skills:
- name: check-balance-and-statement
  slug: banco-inter-check-balance-and-statement
- name: banco-inter-emitir-boleto
  slug: banco-inter-emitir-boleto
- name: issue-bolepix-charge
  slug: banco-inter-issue-bolepix-charge
- name: banco-inter-manage-cobranca
  slug: banco-inter-manage-cobranca
- name: banco-inter-manage-webhook-configuration
  slug: banco-inter-manage-webhook-configuration
- name: manage-webhooks
  slug: banco-inter-manage-webhooks
- name: obtain-access-token
  slug: banco-inter-obtain-access-token
- name: banco-inter-pagar-boleto
  slug: banco-inter-pagar-boleto
- name: pay-with-pix
  slug: banco-inter-pay-with-pix
- name: banco-inter-pix-payment
  slug: banco-inter-pix-payment
- name: setup-pix-automatico
  slug: banco-inter-setup-pix-automatico
slug: banco-inter
tags:
- Company
- Banking
- Fintech
- Payments
- Pix
- Brazil
- Digital Bank
- Open Banking
website: https://bancointer.com.br
---
