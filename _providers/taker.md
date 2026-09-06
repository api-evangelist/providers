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
  - sandbox
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
- description: Delivery-integration API connecting restaurants (Taker GO merchants) and delivery service providers (DSPs). Supports order creation, retrieval, cancellation, DSP re-routing, and asynchronous order-sta
  name: Taker GO Integration API
  slug: taker-go-integration-api
artifact_total: 4
asyncapis:
- description: ''
  name: Taker Webhooks
  slug: taker-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://taker.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.help.taker.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.help.taker.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.help.taker.io/
- group: company
  title: ''
  type: Blog
  url: https://taker.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://taker.io/blog/feed
- group: operate
  title: ''
  type: Support
  url: https://taker.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taker.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taker.io/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/taker-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taker-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/taker-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/taker-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taker-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taker-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/taker-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taker-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taker-domain-security.yml
created: '2026-07-17'
description: Taker is a Riyadh, Saudi Arabia-based restaurant technology company (founded 2018, backed by 500 Global) providing an all-in-one online ordering and restaurant-growth platform used by 1,000+ restaurants. Its product suite spans Taker Channels (branded web/mobile ordering), Taker GO (delivery operations), Taker Flow (operations optimization), Taker Grow (marketing automation), and Taker 360 (a unified dashboard across delivery aggregators). The Taker GO delivery-integration API connects restaurants and delivery service providers (DSPs) with bearer-token auth for order creation, tracking, cancellation, and asynchronous status delivery via webhooks, across published sandbox and production environments.
image: https://taker.io/wp-content/themes/taker-2026/assets/images/logo.svg
layout: provider
modified: '2026-07-21'
name: Taker
nav: Providers
network: true
overview: 'Taker publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant Technology, Online Ordering, Food Delivery, and Delivery Integration.


  The Taker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Taker''s developer surface includes documentation, API reference, engineering blog, support, authentication, sandbox, and 13 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 33.7
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taker/refs/heads/main/screenshots/taker-2026-09-02T162435.png
security:
- kind: authentication
  name: Taker Authentication
  slug: taker-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taker Domain Security
  slug: taker-domain-security
  summary_line: no transport/DNS hardening detected
slug: taker
tags:
- Company
- Restaurant Technology
- Online Ordering
- Food Delivery
- Delivery Integration
- Webhook
- Saudi Arabia
- MENA
website: https://taker.io
---
