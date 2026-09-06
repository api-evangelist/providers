---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.activfinancial.com'', ''status'': 302, ''note'': ''declared website redirects to https://www.options-it.com/ — a different registrable domain (activfinancial.com -> options-it.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: WebSocket/WebAssembly JavaScript API for the ACTIV OnePlatform (Options Atlas), delivering real-time streaming subscriptions, snapshots, queries, and time-series (tick, intraday bar, history bar) mark
  name: ACTIV OnePlatform Web API (One API)
  slug: activ-oneplatform-web-api-one-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.activfinancial.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://weboneapi.activfinancial.com/
- group: docs
  title: ''
  type: Documentation
  url: https://weboneapi.activfinancial.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://weboneapi.activfinancial.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://weboneapi.activfinancial.com/tutorials
- group: start
  title: ''
  type: Sandbox
  url: sandbox/activ-financial-systems-sandbox.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/activfinancial
- group: operate
  title: ''
  type: Support
  url: https://www.options-it.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.options-it.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.options-it.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.options-it.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/activ-financial-systems-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/activ-financial-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/activ-financial-systems-packages.yml
- group: design
  title: ''
  type: Components
  url: components/activ-financial-systems-components.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/activ-financial-systems-error-codes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/activ-financial-systems-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/activ-financial-systems-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/activ-financial-systems-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activ-financial-systems-domain-security.yml
created: '2026-07-17'
description: 'ACTIV Financial Systems is a provider of real-time and historical financial market data, best known for the ACTIV Feed consolidated multi-asset market data feed delivering global equities, options, futures, foreign exchange, and fixed income content with associated analytics and low-latency delivery to trading firms, banks, and financial applications. ACTIV Financial was acquired by Options Technology (Options-IT) in 2021 and its market data capabilities are delivered as part of the Options Atlas platform; www.activfinancial.com now redirects to www.options-it.com. A live public developer surface remains: the OnePlatform Web API (One API), a WebSocket/WebAssembly JavaScript API with a developer portal at weboneapi.activfinancial.com and 25 first-party packages on npm under the @activfinancial scope, with gateway hosts and credentials provisioned per customer rather than self-serve.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/activ-financial-systems.png
layout: provider
modified: '2026-07-22'
name: ACTIV Financial Systems
nav: Providers
network: true
overview: 'ACTIV Financial Systems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Market Data, Financial Data, and Real-Time Data.


  ACTIV Financial Systems'' developer surface includes documentation, API reference, getting-started guide, sandbox, support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 23.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/activ-financial-systems/refs/heads/main/screenshots/activ-financial-systems-2026-07-22T202115.png
security:
- kind: authentication
  name: Activ Financial Systems Authentication
  slug: activ-financial-systems-authentication
  summary_line: credentials · 1 scheme
- kind: domain-security
  name: Activ Financial Systems Domain Security
  slug: activ-financial-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: activ-financial-systems
tags:
- Company
- Fintech
- Market Data
- Financial Data
- Real-Time Data
- Streaming
- WebSocket
- Trading Infrastructure
- Options Technology
website: https://www.activfinancial.com
---
