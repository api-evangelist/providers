---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: 180 Insurance Agentic Access
  operation_count: 33
  slug: 180-insurance-agentic-access
  summary_line: 33 operations · 20 acting
api_count: 1
apis:
- baseURL: https://sagas.staging.180s.com.br
  baseurl_source: declared
  description: The Cotações API from 180 Insurance — 2 operation(s) for cotações.
  name: 180 Insurance Cotações API
  slug: 180-insurance-cota-es-api
- baseURL: https://sagas.staging.180s.com.br
  baseurl_source: declared
  description: The Produtos API from 180 Insurance — 1 operation(s) for produtos.
  name: 180 Insurance Produtos API
  slug: 180-insurance-produtos-api
- baseURL: https://sagas.staging.180s.com.br
  baseurl_source: declared
  description: The Propostas API from 180 Insurance — 7 operation(s) for propostas.
  name: 180 Insurance Propostas API
  slug: 180-insurance-propostas-api
- baseURL: https://sagas.staging.180s.com.br
  baseurl_source: declared
  description: The Renovações API from 180 Insurance — 3 operation(s) for renovações.
  name: 180 Insurance Renovações API
  slug: 180-insurance-renova-es-api
- baseURL: https://sagas.staging.180s.com.br
  baseurl_source: declared
  description: The Sinistros API from 180 Insurance — 8 operation(s) for sinistros.
  name: 180 Insurance Sinistros API
  slug: 180-insurance-sinistros-api
- baseURL: https://sagas.staging.180s.com.br
  baseurl_source: declared
  description: The Vendas API from 180 Insurance — 6 operation(s) for vendas.
  name: 180 Insurance Vendas API
  slug: 180-insurance-vendas-api
- baseURL: https://sagas.staging.180s.com.br
  baseurl_source: declared
  description: The Webhooks API from 180 Insurance — 3 operation(s) for webhooks.
  name: 180 Insurance Webhooks API
  slug: 180-insurance-webhooks-api
artifact_total: 13
asyncapis:
- description: ''
  name: 180 Insurance Webhooks
  slug: 180-insurance-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/agentic-access/180-insurance-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/180-insurance-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/rules/180-insurance-rules.yml
  title: ''
  type: Spectral
  url: rules/180-insurance-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/vocabulary/180-insurance-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/180-insurance-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/lifecycle/180-insurance-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/180-insurance-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/hosts/180-insurance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/180-insurance-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/vendors/180-insurance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/180-insurance-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/scopes/180-insurance-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/180-insurance-scopes.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://180s.com.br/feed/
- group: company
  title: ''
  type: Website
  url: https://180s.com.br
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.180s.com.br/reference/introducao
- group: docs
  title: ''
  type: Documentation
  url: https://docs.180s.com.br/reference/introducao
- group: docs
  title: ''
  type: APIReference
  url: https://docs.180s.com.br/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.180s.com.br/reference/introducao
- group: company
  title: ''
  type: Blog
  url: https://180s.com.br/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://180s.com.br/condicoes-gerais/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://180s.com.br/wp-content/uploads/2026/03/Politica-de-Privacidade-180-Seguros-new.docx-1.pdf
- group: operate
  title: ''
  type: Support
  url: https://180s.com.br/contato/
- group: start
  title: ''
  type: SignUp
  url: https://180s.com.br/contato/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/180seg
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/authentication/180-insurance-authentication.yml
  title: ''
  type: Authentication
  url: authentication/180-insurance-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/conventions/180-insurance-conventions.yml
  title: ''
  type: Conventions
  url: conventions/180-insurance-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/errors/180-insurance-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/180-insurance-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/asyncapi/180-insurance-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/180-insurance-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/mcp/180-insurance-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/180-insurance-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/lifecycle/180-insurance-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/180-insurance-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/conformance/180-insurance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/180-insurance-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://180s.com.br/tecnologia-180/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/data-model/180-insurance-data-model.yml
  title: ''
  type: DataModel
  url: data-model/180-insurance-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/sandbox/180-insurance-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/180-insurance-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/well-known/180-insurance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/180-insurance-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/security/180-insurance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/180-insurance-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/llms/180-insurance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/180-insurance-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: '180 Seguros (180 Insurance) is the first tech-native insurer in Brazil, an SUSEP-authorized insurtech that lets fintechs, digital banks, credit cooperatives and other financial and non-financial businesses embed insurance into their own products through a single API — the Sagas API. The platform covers the full insurance lifecycle: product/combo listing, quotation (cotação), proposal (proposta), sale/policy issuance (venda), endorsements, renewals (renovações) and claims (sinistros), plus HMAC-signed webhooks for real-time visibility. Authentication is OAuth2 client-credentials via Auth0, errors follow RFC 9457 problem-details, and the company publishes a security posture including AICPA SOC 2, LGPD and SUSEP Circular 638 compliance. 180 Seguros is backed by 8VC, Monashees, Dragoneer, Atlantico and Canary, and was added to the API Evangelist network as an 8VC portfolio company.'
image: https://files.readme.io/21b0f8e-small-180_seguros_logo.jpeg
layout: provider
modified: '2026-10-06'
name: 180 Insurance
nav: Providers
network: true
overview: '180 Insurance publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cotações API, Produtos API, Propostas API, and 4 more. Tagged areas include Company, Insurtech, Insurance, Embedded Insurance, and Brazil.


  The 180 Insurance catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  180 Insurance''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 26 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: 180 Insurance API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 2
  slug: 180-insurance-rules
scopes:
- name: 180 Insurance Scopes
  scope_count: 0
  slug: 180-insurance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.3
  facets:
    access_clarity: 26.3
    contract_governance: 35.6
    contract_quality: 53.5
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: BR
      standard: lgpd
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/180-insurance/refs/heads/main/screenshots/180-insurance-2026-07-25T181107.png
security:
- kind: authentication
  name: 180 Insurance Authentication
  slug: 180-insurance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: 180 Insurance Domain Security
  slug: 180-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 180-insurance
tags:
- Company
- Insurtech
- Insurance
- Embedded Insurance
- Brazil
- Fintech
- Webhook
website: https://180s.com.br
---
