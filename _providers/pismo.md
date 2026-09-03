---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Pismo Agentic Access
  operation_count: 22
  slug: pismo-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Core-banking account lifecycle and balances.
  name: Pismo Accounts API
  slug: pismo-accounts-api
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Card-network authorizations and simulation.
  name: Pismo Authorizations API
  slug: pismo-authorizations-api
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Card issuing and lifecycle.
  name: Pismo Cards API
  slug: pismo-cards-api
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Customer registration and customer-account relationships.
  name: Pismo Customers API
  slug: pismo-customers-api
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Client webhook registration for the Pismo event stream.
  name: Pismo Events API
  slug: pismo-events-api
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Product program configuration.
  name: Pismo Programs API
  slug: pismo-programs-api
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Account statements and statement transactions.
  name: Pismo Statements API
  slug: pismo-statements-api
- baseURL: https://api.pismo.io
  baseurl_source: declared
  description: Posted transactions and transaction shifts.
  name: Pismo Transactions API
  slug: pismo-transactions-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pismo Accounts API
  slug: open-pismo-accounts-api
- collection_type: open
  name: Pismo Accounts Authorizations API
  slug: open-pismo-authorizations-api
- collection_type: open
  name: Pismo Accounts Cards API
  slug: open-pismo-cards-api
- collection_type: open
  name: Pismo Accounts Customers API
  slug: open-pismo-customers-api
- collection_type: open
  name: Pismo Accounts Events API
  slug: open-pismo-events-api
- collection_type: open
  name: Pismo Accounts Programs API
  slug: open-pismo-programs-api
- collection_type: open
  name: Pismo Accounts Statements API
  slug: open-pismo-statements-api
- collection_type: open
  name: Pismo Accounts Transactions API
  slug: open-pismo-transactions-api
- collection_type: open
  name: Pismo API
  slug: open-pismo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/pismo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pismo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pismo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pismo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pismo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pismo-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pismo
- group: company
  title: ''
  type: Website
  url: https://www.pismo.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pismo.io
- group: commercial
  title: ''
  type: Plans
  url: plans/pismo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pismo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pismo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.pismo.io/blog/
created: '2026-06-21'
description: Pismo is a cloud-native issuer-processing and core-banking platform exposing REST APIs for accounts, customers, cards, authorizations, transactions, statements, and programs, plus an event stream (Kafka-backed, delivered via webhooks and cloud event buses). Acquired by Visa in January 2024, Pismo powers card issuing and digital banking for financial institutions across the Americas, Europe, and APAC.
finops:
- name: Pismo Finops
  service_category: Financial Services Platform
  slug: pismo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pismo.png
layout: provider
modified: '2026-06-21'
name: Pismo
nav: Providers
network: true
overview: 'Pismo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authorizations API, Cards API, and 5 more. Tagged areas include Banking, Card Issuing, Payments, Fintech, and Core Banking.


  Pismo''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Pismo Plans Pricing
  plan_count: 1
  slug: pismo-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Pismo Rate Limits
  slug: pismo-rate-limits
scopes:
- name: Pismo Scopes
  scope_count: 3
  slug: pismo-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 47.2
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pismo/refs/heads/main/screenshots/pismo-2026-09-02T151328.png
security:
- kind: authentication
  name: Pismo Authentication
  slug: pismo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pismo Domain Security
  slug: pismo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pismo Vulnerability Disclosure
  slug: pismo-vulnerability-disclosure
  summary_line: disclosure policy published
slug: pismo
tags:
- Banking
- Card Issuing
- Payments
- Fintech
- Core Banking
- Cloud-Native
website: https://www.pismo.io
---
