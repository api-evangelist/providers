---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
api_count: 9
apis:
- description: 'REST/JSON API for the Conta Azul ERP, organized by functional area (Financeiro, Cobranças, Baixas, Vendas, Pessoas, Produtos, Serviços, Notas Fiscais, Contratos), secured with OAuth 2.0 Authorization '
  name: Conta Azul API
  slug: conta-azul-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Categorias API from Conta Azul — 2 operation(s) for categorias.
  name: Conta Azul Categorias API
  slug: conta-azul-categorias-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Centro De Custo API from Conta Azul — 1 operation(s) for centro de custo.
  name: Conta Azul Centro De Custo API
  slug: conta-azul-centro-de-custo-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Conta Financeira API from Conta Azul — 2 operation(s) for conta financeira.
  name: Conta Azul Conta Financeira API
  slug: conta-azul-conta-financeira-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Contratos API from Conta Azul — 4 operation(s) for contratos.
  name: Conta Azul Contratos API
  slug: conta-azul-contratos-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Financeiro API from Conta Azul — 14 operation(s) for financeiro.
  name: Conta Azul Financeiro API
  slug: conta-azul-financeiro-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Orcamentos API from Conta Azul — 2 operation(s) for orcamentos.
  name: Conta Azul Orcamentos API
  slug: conta-azul-orcamentos-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Produto API from Conta Azul — 4 operation(s) for produto.
  name: Conta Azul Produto API
  slug: conta-azul-produto-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Protocolo API from Conta Azul — 1 operation(s) for protocolo.
  name: Conta Azul Protocolo API
  slug: conta-azul-protocolo-api
- baseURL: https://api-v2.contaazul.com
  baseurl_source: declared
  description: The Venda API from Conta Azul — 8 operation(s) for venda.
  name: Conta Azul Venda API
  slug: conta-azul-venda-api
artifact_total: 23
collections:
- collection_type: open
  name: Baixas v1 API
  slug: open-conta-azul-v1-api
common:
- group: commercial
  href: https://artifacts.apis.io/conta-azul/plans/conta-azul-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/conta-azul-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/conta-azul/rate-limits/dvpj-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dvpj-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://contaazul.com/blog/
- group: other
  href: https://artifacts.apis.io/conta-azul/capabilities/conta-azul-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/conta-azul-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/conta-azul/overlays/conta-azul-acquittance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/conta-azul-acquittance-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/conta-azul/security/conta-azul-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conta-azul-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.contaazul.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.contaazul.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.contaazul.com/docs/financial-apis-openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.contaazul.com/guide
- group: auth
  href: https://artifacts.apis.io/conta-azul/authentication/conta-azul-authentication.yml
  title: ''
  type: Authentication
  url: authentication/conta-azul-authentication.yml
- group: auth
  href: https://artifacts.apis.io/conta-azul/scopes/conta-azul-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/conta-azul-scopes.yml
- group: agent
  href: https://artifacts.apis.io/conta-azul/well-known/conta-azul-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/conta-azul-well-known.yml
- group: design
  href: https://artifacts.apis.io/conta-azul/conventions/conta-azul-conventions.yml
  title: ''
  type: Conventions
  url: conventions/conta-azul-conventions.yml
- group: design
  href: https://artifacts.apis.io/conta-azul/errors/conta-azul-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/conta-azul-problem-types.yml
- group: design
  href: https://artifacts.apis.io/conta-azul/lifecycle/conta-azul-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/conta-azul-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contaazul.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.contaazul.com/migration
- group: operate
  href: https://artifacts.apis.io/conta-azul/changelog/conta-azul-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/conta-azul-changelog.yml
- group: design
  href: https://artifacts.apis.io/conta-azul/data-model/conta-azul-data-model.yml
  title: ''
  type: DataModel
  url: data-model/conta-azul-data-model.yml
- group: agent
  href: https://artifacts.apis.io/conta-azul/mcp/conta-azul-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/conta-azul-mcp.yml
- group: agent
  href: https://artifacts.apis.io/conta-azul/llms/conta-azul-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conta-azul-llms.txt
- group: design
  href: https://artifacts.apis.io/conta-azul/conformance/conta-azul-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conta-azul-conformance.yml
- group: build
  href: https://artifacts.apis.io/conta-azul/packages/conta-azul-packages.yml
  title: ''
  type: Packages
  url: packages/conta-azul-packages.yml
- group: agent
  href: https://artifacts.apis.io/conta-azul/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://ajuda.contaazul.com/hc/pt-br
- group: company
  title: ''
  type: Blog
  url: https://blog.contaazul.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ContaAzul
- group: commercial
  title: ''
  type: Pricing
  url: https://contaazul.com/planos/
- group: start
  title: ''
  type: SignUp
  url: https://developers-portal.contaazul.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contaazul.com/termos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contaazul.com/termos/privacidade/
- group: company
  title: ''
  type: Website
  url: https://contaazul.com
created: '2026-07-17'
description: 'Conta Azul is a Brazilian cloud accounting, financial-management and ERP platform for small and medium businesses, backed by Ribbit Capital. Its Nova API (v2, api-v2.contaazul.com) exposes the ERP over REST/JSON with OAuth 2.0 (AWS Cognito) authorization: financial events (accounts payable and receivable), installments, cost centers, categories and DRE, financial accounts and balances, sales, charges, products/inventory, proposals, contracts and settlements (baixas). The legacy API was sunset in November 2025 in favor of this versioned, OpenAPI-documented platform.'
finops:
- has_sources: true
  method: derived
  name: Conta Azul Finops
  primary_unit: ''
  service_category: ''
  slug: conta-azul-finops
  template: true
image: https://contaazul.com/wp-content/themes/contaazul/assets/images/logo.svg
layout: provider
modified: '2026-10-06'
name: Conta Azul
nav: Providers
network: true
overview: 'Conta Azul publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Categorias API, Centro De Custo API, Conta Financeira API, and 7 more. Tagged areas include Company, Fintech, Accounting, ERP, and Brazil.


  The Conta Azul catalog on APIs.io includes 1 Spectral governance ruleset.


  Conta Azul''s developer surface includes engineering blog, documentation, API reference, getting-started guide, authentication, changelog, support, and 26 more developer resources.'
plans:
- name: Conta Azul Plans Pricing
  plan_count: 4
  slug: conta-azul-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Dvpj Rate Limits
  slug: dvpj-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Conta Azul API Rules
  rule_count: 59
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 11
  slug: conta-azul-rules
scopes:
- name: Conta Azul Scopes
  scope_count: 3
  slug: conta-azul-scopes
  summary_line: 3 scopes · authorizationCode
- name: Dvpj Scopes
  scope_count: 3
  slug: dvpj-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 51.8
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 58.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 33.3
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: BR
      standard: lgpd
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/conta-azul/conta-azul-2026-07-25T210322.png
security:
- kind: authentication
  name: Conta Azul Authentication
  slug: conta-azul-authentication
  summary_line: oauth2/http · 2 schemes
- kind: authentication
  name: Dvpj Authentication
  slug: dvpj-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Conta Azul Domain Security
  slug: conta-azul-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: Look up a product and create a sale
  slug: conta-azul-create-sale
- name: Issue a charge and check its status
  slug: conta-azul-issue-charge
- name: Record a receivable and settle it
  slug: conta-azul-record-and-settle-receivable
slug: conta-azul
tags:
- Company
- Fintech
- Accounting
- ERP
- Brazil
- Small Business
- Financial Management
- Invoicing
- Payments
website: https://contaazul.com
---
