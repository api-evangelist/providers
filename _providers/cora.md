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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Cora Agentic Access
  operation_count: 20
  slug: cora-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 16
apis:
- description: 'Cora''s transactional banking API for Direct Integration: registered boleto and carnê (installment) issuance, Pix QR codes, account data, balance and statement queries, payment and transfer initiation '
  name: Cora API
  slug: cora-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Balance API from Cora — 1 operation(s) for balance.
  name: Cora Balance API
  slug: cora-balance-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Banks API from Cora — 1 operation(s) for banks.
  name: Cora Banks API
  slug: cora-banks-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Boletos V2 API from Cora — 3 operation(s) for boletos v2.
  name: Cora Boletos V2 API
  slug: cora-boletos-v2-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Businesses API from Cora — 3 operation(s) for businesses.
  name: Cora Businesses API
  slug: cora-businesses-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Credentials API from Cora — 1 operation(s) for credentials.
  name: Cora Credentials API
  slug: cora-credentials-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Dados De Conta API from Cora — 1 operation(s) for dados de conta.
  name: Cora Dados De Conta API
  slug: cora-dados-de-conta-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Initiate API from Cora — 1 operation(s) for initiate.
  name: Cora Initiate API
  slug: cora-initiate-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Issuer API from Cora — 1 operation(s) for issuer.
  name: Cora Issuer API
  slug: cora-issuer-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Notificações API from Cora — 1 operation(s) for notificações.
  name: Cora Notificações API
  slug: cora-notifica-es-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Notifications API from Cora — 1 operation(s) for notifications.
  name: Cora Notifications API
  slug: cora-notifications-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Pagamento De Impostos API from Cora — 1 operation(s) for pagamento de impostos.
  name: Cora Pagamento De Impostos API
  slug: cora-pagamento-de-impostos-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Pay API from Cora — 1 operation(s) for pay.
  name: Cora Pay API
  slug: cora-pay-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Service Receipt API from Cora — 1 operation(s) for service receipt.
  name: Cora Service Receipt API
  slug: cora-service-receipt-api
- baseURL: https://matls-clients.api.cora.com.br
  baseurl_source: declared
  description: The Statement API from Cora — 1 operation(s) for statement.
  name: Cora Statement API
  slug: cora-statement-api
artifact_total: 21
asyncapis:
- description: ''
  name: Cora Webhooks
  slug: cora-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/agentic-access/cora-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cora-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/rules/cora-rules.yml
  title: ''
  type: Spectral
  url: rules/cora-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/errors/cora-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cora-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/hosts/cora-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cora-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/integrations/cora-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cora-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/vendors/cora-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cora-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cora.com.br/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/scopes/cora-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cora-scopes.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cora.com.br/blog/feed/
- group: company
  title: ''
  type: Website
  url: https://www.cora.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cora.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cora.com.br/docs/instrucoes-iniciais
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cora.com.br/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cora.com.br/docs/instrucoes-iniciais
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/authentication/cora-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cora-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cora.com.br/changelog/welcome-to-cora-api
- group: company
  title: ''
  type: Blog
  url: https://www.cora.com.br/blog/
- group: operate
  title: ''
  type: Support
  url: https://meajuda.cora.com.br/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cora.com.br/integracoes/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cora.com.br/termos-e-condicoes-de-apis/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/corabank/cora-s-public-workspace/documentation/ppi1okk/api-cora
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/llms/cora-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cora-llms.txt
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/sandbox/cora-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cora-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/conventions/cora-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cora-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/conventions/cora-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cora-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/asyncapi/cora-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cora-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/lifecycle/cora-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cora-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/changelog/cora-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cora-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/conformance/cora-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cora-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/security/cora-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cora-domain-security.yml
created: '2026-07-17'
description: Cora is a Brazilian digital bank (conta PJ) for small and medium businesses, offering fee-free business checking, Pix, boletos, transfers, payment initiation and financial management. Its developer platform exposes REST APIs for registered boleto and carnê issuance, Pix QR code generation, account data, balance and statement queries, payment and transfer initiation (including DARF and GPS tax payments), webhook notifications, and municipal service invoice (NFS-e) issuance. Cora offers two integration modalities — Direct Integration (mutual-TLS certificate plus OAuth2 client-credentials) and Cora Partnership — with a Stage sandbox for testing. Backed by QED Investors and Ribbit Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cora.png
layout: provider
modified: '2026-10-06'
name: Cora
nav: Providers
network: true
overview: 'Cora publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Banks API, Boletos V2 API, and 12 more. Tagged areas include Company, Banking, Brazil, Payments, and Pix.


  The Cora catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cora''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 23 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Cora API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 3
  slug: cora-rules
scopes:
- name: Cora Scopes
  scope_count: 0
  slug: cora-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.0
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 56.2
    developer_ergonomics: 42.9
    discoverability: 80.4
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 34.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/screenshots/cora-2026-07-25T210413.png
security:
- kind: authentication
  name: Cora Authentication
  slug: cora-authentication
  summary_line: oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Cora Domain Security
  slug: cora-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cora
tags:
- Company
- Banking
- Brazil
- Payments
- Pix
- Boleto
- Invoicing
- Small Business
- Fintech
- Banking as a Service
website: https://www.cora.com.br/
---
