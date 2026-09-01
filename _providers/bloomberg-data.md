---
access_model:
  confidence: high
  label: Enterprise Contract
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - https://professional.bloomberg.com/products/data/data-license/
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Provides access to Bloomberg's extensive financial data including real-time quotes, historical data, reference data, and analytics.
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: Real-time streaming market data API delivering quotes, trades, and market depth.
  name: Bloomberg B-PIPE API
  slug: bloomberg-b-pipe-api
artifact_total: 9
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-data-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloomberg-data-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloomberg-data-security.txt
- group: auth
  title: ''
  type: Security
  url: security/bloomberg-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-data-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bloomberg-data-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bloomberg-data-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bloomberg-data-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bloomberg-data-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/bloomberg-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bloomberg-data-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloomberg-data-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/bloomberg-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bloomberg-data-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://bloomberg.github.io/blpapi-docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: start
  title: ''
  type: Login
  url: https://console.blpprofessional.com/
created: '2024-01-01'
description: 'Bloomberg''s enterprise market-data API surface. The Data License / Hypermedia (HAPI) REST API on api.bloomberg.com delivers reference, pricing, regulatory, ESG, fundamentals, estimates and historical content — 100B+ data points a day across 70M+ instruments, 40k+ fields and 8k+ datasets — request/response and by subscription, alongside SFTP and native cloud delivery. B-PIPE delivers real-time streaming quotes, trades and market depth, consumed not over HTTP but through the BLPAPI SDK over a TCP session against a customer-provisioned appliance. Both are contracted enterprise products: there is no self-service signup, no published pricing, and no public machine-readable contract, though Bloomberg does publish OAuth protected-resource and authorization-server metadata.'
finops:
- name: Bloomberg Data Finops
  service_category: API
  slug: bloomberg-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-data.png
layout: provider
modified: '2026-08-27'
name: Bloomberg Data
nav: Providers
network: true
overview: 'Bloomberg Data publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Financial-Services, Market Data, News, and Real-Time Data.


  Bloomberg Data''s developer surface includes developer portal, documentation, support, authentication, API reference, and 19 more developer resources.'
plans:
- name: Bloomberg Data Plans Pricing
  plan_count: 0
  slug: bloomberg-data-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Bloomberg Data Rate Limits
  slug: bloomberg-data-rate-limits
scopes:
- name: Bloomberg Data Scopes
  scope_count: 0
  slug: bloomberg-data-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 33.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-data/refs/heads/main/screenshots/bloomberg-data-2026-06-20T173410.png
security:
- kind: authentication
  name: Bloomberg Data Authentication
  slug: bloomberg-data-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Bloomberg Data Domain Security
  slug: bloomberg-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Data Vulnerability Disclosure
  slug: bloomberg-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-data
tags:
- Analytics
- Financial-Services
- Market Data
- News
- Real-Time Data
- Trading
website: https://developer.bloomberg.com/
---
