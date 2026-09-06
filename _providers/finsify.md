---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RESTful bank-aggregation API for accessing consumer banking data — accounts, balances, and categorized transaction history — plus customer, connection token, and login lifecycle management, with webho
  name: Finsify Hub API
  slug: finsify-hub-api
artifact_total: 4
asyncapis:
- description: ''
  name: Finsify Webhooks
  slug: finsify-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://hub.finsify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.finsify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finsify.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.finsify.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/finsify-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finsify-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/finsify-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finsify-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finsify-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finsify-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/finsify-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finsify-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finsify-domain-security.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/finsify-service-catalog.json
created: '2026-07-17'
description: Finsify is a Southeast Asian bank-data aggregation company whose Finsify Hub service exposes a RESTful API for accessing end-user banking data — account balances and status, and categorized transaction history — across 50+ bank and statement services in 15 countries. The API handles customer creation, short-lived connection tokens that drive the end-user bank-login flow, account retrieval, transaction history filtered by date range, and login lifecycle management (activate, deactivate, refresh, reconnect), with machine-learning transaction categorization and webhook notifications for new transactions and login-status changes. Finsify is a 500 Global portfolio company and powers fintech products including Money Lover, Money Paper, Ngan Luong, and Bao Kim.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finsify.png
layout: provider
modified: '2026-07-19'
name: Finsify
nav: Providers
network: true
overview: 'Finsify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Open Banking, Bank Aggregation, and Financial Data.


  The Finsify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finsify''s developer surface includes documentation, API reference, authentication, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 24.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finsify/refs/heads/main/screenshots/finsify-2026-07-25T214546.png
security:
- kind: authentication
  name: Finsify Authentication
  slug: finsify-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Finsify Domain Security
  slug: finsify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: finsify
tags:
- Company
- Financial-Services
- Open Banking
- Bank Aggregation
- Financial Data
- Transaction
- Fintech
- Southeast Asia
website: https://hub.finsify.com
---
