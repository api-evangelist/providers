---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: JSON REST API for authentication, users/KYC, balances, beneficiaries, collections, collection requests, conversions, currencies, deductions, funding, internal transfers, payments, and webhook notifica
  name: Wallex Partner API
  slug: wallex-partner-api
artifact_total: 5
asyncapis:
- description: ''
  name: Wallex Webhooks
  slug: wallex-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://wallex.asia
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wallex.asia/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wallex.asia/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wallex.asia/docs/api/authentication/authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wallex.asia/docs/send-first-payment
- group: operate
  title: ''
  type: Support
  url: https://help.wallex.asia/
- group: auth
  title: ''
  type: Authentication
  url: authentication/wallex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wallex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wallex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wallex-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wallex-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wallex-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wallex-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wallex-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wallex-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wallex-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wallex-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wallex-llms.txt
created: '2026-07-17'
description: Wallex is a Singapore-headquartered cross-border payments and business banking platform for businesses across Southeast Asia and Greater China. Its Partner API is a JSON REST API that lets platforms embed multi-currency wallets, issue virtual collection accounts, run FX conversions, send cross-border payments to beneficiaries, and onboard and KYC their own members. The API is organised around a hierarchical account model (Standard and Partner accounts, Individual and Company entities, Regular and Lite KYC) and covers authentication, balances, beneficiaries, collections, collection requests, conversions, currencies, deductions, funding, internal transfers, payments, users, and webhooks. Wallex is a portfolio company of 500 Global.
image: https://docs.wallex.asia/img/wallex-icon.png
layout: provider
modified: '2026-07-21'
name: Wallex
nav: Providers
network: true
overview: 'Wallex publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Foreign Exchange, and Fintech.


  The Wallex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wallex''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 13 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 2
  name: Wallex Rate Limits
  slug: wallex-rate-limits
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 25.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 26.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wallex/refs/heads/main/screenshots/wallex-2026-09-02T170414.png
security:
- kind: authentication
  name: Wallex Authentication
  slug: wallex-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wallex Domain Security
  slug: wallex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: wallex
tags:
- Company
- Payments
- Cross-Border Payments
- Foreign Exchange
- Fintech
- Collection
- B2B Payments
- Embedded Finance
- Southeast Asia
website: https://wallex.asia
---
